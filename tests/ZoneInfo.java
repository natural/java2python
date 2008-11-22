/* Copyright (C) 1999 Business Management Systems, Inc.

This code is distributed under the GNU Library General Public License.

http://www.gnu.org/copyleft/lgpl.html

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA  02111-1307, USA.

 * $Log: ZoneInfo.java,v $
 * Revision 1.11  2006/05/10 16:47:17  stuart
 * Make TZType and ZoneInfo Serializable, thanks to Eric Goff.
 *
 * Revision 1.10  2004/12/08 00:24:04  stuart
 * Misspelled System.currentTimeMillis()
 *
 * Revision 1.9  2004/12/08 00:20:42  stuart
 * Find better default timezone, suggested by Ophir Bleiberg.
 *
 * Revision 1.8  2003/03/07 00:11:36  stuart
 * Bug fix from Dave Jarvis: Close zoneinfo file after reading.
 * Changes suggested by Shawn Potter:
 *   Removed dependency on shareware Lava Rocks sprintf classes,
 *     uses java.text.DecimalFormat instead.
 *   Commented out System.err.println in inDaylightTime() method.
 *   Changed default timezone file location to more standard location
 *     "/usr/share/zoneinfo".
 *
 * Revision 1.7  2003/03/06 22:17:00  stuart
 * use 64-bit timestamps for 2038 readiness
 *
 * Revision 1.6  2000/06/05  03:22:28  stuart
 * dump /etc/localtime by default
 *
 * Revision 1.5  1999/07/15  03:27:00  stuart
 * Rename to ZoneInfo
 *
 * Revision 1.4  1999/07/14  04:45:22  stuart
 * tm_offset unused
 *
 * Revision 1.3  1999/07/14  04:42:07  stuart
 * more docs, set proper timezone ID
 * TZDump takes timezones to dump as args
 *
 * Revision 1.2  1999/07/14  03:26:28  stuart
 * tested with GregorianCalendar
 *
 */
package bmsi.util;

import java.io.*;
import java.util.TimeZone;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Calendar;
import java.text.DateFormat;
import java.text.DecimalFormat;

/** Timezone type description.  E.g. EST or EDT.
  This should be an inner class, but 1.1 JDK compiler freaks out
  when using blank final with inner classes.  It is permissible
  for a package private class not used from any other class in the
  package to be in the same source file.  However, some java IDE tools
  freak out over this.
    @author Stuart D. Gathman
 */
class TZType implements Serializable {
  private static final long serialVersionUID = 1L;
  /** Offset from GMT in seconds. */
  public final int offset;
  /** Name of type. */
  public final String name;
  /** True if daylight savings time. */
  public final boolean isdst;

  TZType(String name,int offset,boolean dst) {
    this.name = name;
    this.offset = offset;
    this.isdst = dst;
  }

  public String toString() {
    return "TzType: "+name+" : offs="+offset+" dst="+isdst;
  }
}

/** Reads timezone information from /etc/zoneinfo.  Implements the
    <code>java.util.TimeZone</code> interface and also provides
    work alikes for unix time conversion functions.  Unlike 
    <code>java.util.SimpleTimeZone</code>, this implementation
    supports historical daylight savings time changes and leap seconds.
    <p>
    Unfortunately, the TimeZone API does not support giving a unique
    name to positive leap seconds (for example, 1998 Dec 31 23:59:60 UTC).
    As a result, a positive leap second has the same HMS representation
    as the previous second when using <code>java.util.GregorianCalendar</code>.
    <p>
    Even more unfortunately, <code>java.text.SimpleDateFormat</code>
    decides which TimeZone name to use by comparing the
    <code>DST_OFFSET</code> calendar field to zero.  
    <code>GregorianCalendar</code> computes this by subtracting 
    <code>getRawOffset()</code> from <code>getOffset()</code>.
    Of course, these are never equal once leapseconds kick in, so 
    beginning in 1972, SimpleDateFormat always (incorrectly) uses the
    daylight time abbreviation with this TimeZone implementation.
    <p>
    This code is based loosely
    on the unix localtime package version 4.1.  Rules for each timezone
    are stored in binary form 
    in the <code>/etc/zoneinfo</code> directory.  These binary files are
    produced by the zoneinfo compiler, <code>zic</code>, included with the
    localtime package as C source.  I have not yet ported the compiler
    to Java.  The format accomodates
    historical timezone changes (e.g. war time and the 1987 change in the US),
    and leapseconds.  
    <p>
    Localtime format uses signed 32-bit values, so it peters
    out in 2038.  This can be extended by noting that
    each table has monotonically increasing keys - hence the high order bits 
    can be implied.  However, timezone changes are listed exhaustively (rules
    are interpreted by the zoneinfo compiler), so the tables would be
    quite large if extended to the full range of 64-bit Java time values.
    I propose that the timezone files can be gradually extended, becoming
    larger and larger as required, until a better solution is invented.  
    There is no point at which things suddenly break.
    <p>
    I have not yet implemented the implicitly extended table, so this
    version will break with regards to determining daylight savings time
    and accumulating leapseconds beginning in 2039.  The main purpose
    of this implementation is to point out deficiences in the
    JDK classes.  Another deficiency not mentioned above is that
    a TimeZone can have more than two abbreviations.  For example, 
    Eastern time includes EST,EDT,EWT.
    <p>
    The best way to make this actually useful, besides extending the range
    beyond 2038, is probably to extend, fix, or replace GregorianCalendar
    (to support minutes with leap seconds and the correct DST_OFFSET).
    The two abbreviation limit can be fixed by adding a ZONE_INDEX
    field to <code>java.util.Calendar</code> and using it in 
    <code>SimpleDateFormat</code>.

    @author Stuart D. Gathman
    Copyright (C) 1998 Business Management Systems, Inc.
 */
public class ZoneInfo extends TimeZone {
  private static final long serialVersionUID = 1L;
  private int[] transTimes;	// transition times
  private byte[] transTypes;	// timezone description for each transition
  private TZType[] tz;		// timezone descriptions
  private int[] leapSecs;	// leapseconds
  private int rawoff = 0;
  private TZType normaltz; 

  /** Initializes timezone info from a File in the tzfile format. */
  public ZoneInfo(File f) throws IOException {
    DataInputStream ds = new DataInputStream(new BufferedInputStream(
    	new FileInputStream(f)));

    try {
      // read header
      ds.skip(28);
      int leapcnt = ds.readInt();
      int timecnt = ds.readInt();
      int typecnt = ds.readInt();
      int charcnt = ds.readInt();

      // load DST transition data
      transTimes = new int[timecnt];
      for (int i = 0; i < timecnt; ++i)
	transTimes[i] = ds.readInt();
      transTypes = new byte[timecnt];
      ds.readFully(transTypes);

      // load TZ type data
      int[] offset = new int[typecnt];
      byte[] dst = new byte[typecnt];
      byte[] idx = new byte[typecnt];
      for (int i = 0; i < typecnt; ++i) {
	offset[i] = ds.readInt();
	dst[i] = ds.readByte();
	idx[i] = ds.readByte();
      }
      byte[] str = new byte[charcnt];
      ds.readFully(str);

      // convert type data
      tz = new TZType[typecnt];
      for (int i = 0; i < typecnt; ++i) {
	// find string
	int pos = idx[i];
	int end = pos;
	while (str[end] != 0) ++end;
	tz[i] = new TZType(new String(str,pos,end-pos),offset[i],dst[i] != 0);
      }

      // load leap seconds table
      leapSecs = new int[leapcnt * 2];
      for (int i = 0; leapcnt > 0; --leapcnt) {
	leapSecs[i++] = ds.readInt();
	leapSecs[i++] = ds.readInt();
      }
    }
    finally { ds.close(); }

    // Set default timezone (normaltz).
    // First, set default to first non-DST rule.
    int n = 0;
    while (tz[n].isdst && n < tz.length)
      ++n;
    normaltz = tz[n];

    // When setting "normaltz" (the default timezone) in the constructor,
    // we originally took the first non-DST rule for the current TZ.
    // But this produces nonsensical results for areas where historical
    // non-integer time zones were used, e.g. if GMT-2:33 was used until 1918.

    // This loop, based on a suggestion by Ophir Bleibergh, tries to find a
    // non-DST rule close to the current time. This is somewhat of a hack, but
    // much better than the previous behavior in this case.

    // Tricky: we need to get either the next or previous non-dst TZ
    // We shall take the future non-dst value, by trying to add 3 months at a
    // time to the current date and searching.
    final long ts = System.currentTimeMillis() / 1000;
    for (int i = 0; i < 9; i++) {
      TZType currTz = getTZ(ts + secsPerThreeMonths*i);
      if (!currTz.isdst) {
	normaltz = currTz;
	break;
      }
    }

    setID(normaltz.name);
  }

  private static final long secsPerThreeMonths = 60*60*24*30*3;

  /** Return the ZoneInfo for local time on this machine.  For unix,
     we read /etc/localtime, which is a link to the proper zoneinfo file. */
  public ZoneInfo() throws IOException {
    this(new File("/etc/localtime"));
  }

  /** Return the ZoneInfo for a timezone name.  For unix, read
     /usr/share/zoneinfo/tzname.
   @param tzname	the name of the timezone to read
   */
  public ZoneInfo(String tzname) throws IOException {
    this(new File("/usr/share/zoneinfo",tzname));
  }

  public int getRawOffset() {
    return normaltz.offset * 1000 + rawoff;
  }

  public void setRawOffset(int millis) {
    rawoff = millis - normaltz.offset * 1000;
  }

  /** Return the offset from UT for a calendar date and time.
      The calendar time we are passed is always computed using
      getRawOffset().
   */
  public int getOffset(int era,int year,int month,int day,int dow,int millis) {
    if (era != GregorianCalendar.AD) 
      return getRawOffset();
    int secs = millis/1000;
    tm then = new tm(year - 1900,month,day,secs);
    long ts;
    try {
      ts = mktime(then,true);
    }
    catch (IllegalArgumentException x) {
      // outside the range of mktime
      return getRawOffset();
    }
    int offset = getTZ(ts).offset;
    for (int y = leapSecs.length; (y-=2) >= 0; ) {
      int ls_trans = leapSecs[y];
      int ls_corr = leapSecs[y+1];
      if (ts >= ls_trans) {
	offset -= ls_corr;
	break;
      }
    }
    return offset * 1000 + rawoff;
  }

  /** Return true if a particular instant is considered part of daylight
      time in this timezone. */
  public boolean inDaylightTime(Date d) {
    TZType tz = getTZ((int)(d.getTime()/1000));
    //System.err.println("isdst = " + tz.isdst);
    return tz.isdst;
  }

  /** Return true if this timezone has transitions between various offsets
      from UT, such as standard time and daylight time.
  */
  public boolean useDaylightTime() {
    return tz.length > 1;
  }
 
  private static final int SECSPERMIN	= 60;
  private static final int MINSPERHOUR	= 60;
  private static final int HOURSPERDAY	= 24;
  private static final int DAYSPERWEEK	= 7;
  private static final int SECSPERHOUR	= SECSPERMIN * MINSPERHOUR;
  private static final int SECSPERDAY	= SECSPERHOUR * HOURSPERDAY;
  private static final int TM_SUNDAY	= 0;
  private static final int TM_MONDAY	= 1;
  private static final int TM_TUESDAY	= 2;
  private static final int TM_WEDNESDAY	= 3;
  private static final int TM_THURSDAY	= 4;
  private static final int TM_FRIDAY	= 5;
  private static final int TM_SATURDAY	= 6;
  private static final int EPOCH_WDAY	= TM_THURSDAY;
  private static final int EPOCH_YEAR	= 1970;

  private static final int DAYSADJ = 25203;	// days between 1900 & 1970
  private static final int CENT_WDAY 	= EPOCH_WDAY - DAYSADJ % 7;

  /** Local time variables. */
  public static class tm {
    /* Second of day. */
    //public int tm_secs;
    /** Hour of day, 0 - 23. */
    public int tm_hour;
    /** Minute of hour, 0 - 59. */
    public int tm_min;
    /** Second of minute, 0 - 60.  
        Note that value may be 60 on a leap second. */
    public int tm_sec;
    /** Day of week, 0 - 6, 0 = Sunday */
    public int tm_wday;
    /** Years since 1900. */
    public int tm_year;
    /** Day of year, 1 - 366. */
    public int tm_yday;
    /** Month of year, 0 - 11. */
    public int tm_mon;
    /** Day of month, 1 - 31. */
    public int tm_mday;
    /** True if time is DST. */
    public boolean tm_isdst;
    /** Timezone name. */
    public String tm_zone;

    private static final DecimalFormat f = new DecimalFormat("#0");
    private static final DecimalFormat f0 = new DecimalFormat("00");

    public String toString() {
      return f.format(tm_mon + 1) + '/' + f0.format(tm_mday) 
	+ '/' + f0.format(tm_year + 1900)
	+ ' ' + f.format(tm_hour) + ':' + f0.format(tm_min)
	+ ':' + f0.format(tm_sec) + ' ' + (tm_zone == null ? "NUL" : tm_zone)
      ;
    }

    public tm() { }

    /** Initialize a new tm object to calendar day and time offset.
      @param year	years since 1900
      @param mon	month 0-11
      @param day	day of month 1-31
      @param secs	seconds in day
     */
    public tm(int year,int mon,int day,int tm_secs) {
      tm_year = year;
      tm_mon = mon;
      tm_mday = day;
      setSecs(tm_secs);
    }

    public void setSecs(int tm_secs) {
      //this.tm_secs = tm_secs;
      tm_hour = tm_secs / SECSPERHOUR;
      int rem = tm_secs % SECSPERHOUR;
      tm_min =  rem / SECSPERMIN;
      tm_sec = rem % SECSPERMIN;
    }

    public int compareTo(tm t) {
      if (tm_year != t.tm_year)
        return tm_year - t.tm_year;
      if (tm_mon != t.tm_mon)
        return tm_mon - t.tm_mon;
      if (tm_mday != t.tm_mday)
        return tm_mday - t.tm_mday;
      if (tm_hour != t.tm_hour)
        return tm_hour - t.tm_hour;
      if (tm_min != t.tm_min)
        return tm_min - t.tm_min;
      return tm_sec - t.tm_sec;
      //return tm_secs - t.tm_secs;
    }

    public boolean equals(Object obj) {
      return (obj instanceof tm) && compareTo((tm)obj) == 0;
    }

    public int hashCode() {
      return (tm_year<<24)+(tm_mon<<20)+(tm_mday<<15)
      	+(tm_hour<<10)+(tm_min<<5)+tm_sec;
    }

    /** Set the local time fields from a clock and GMT offset.
        @param clock	seconds since 1970
	@param offset	offset from UT in seconds
     */
    public void setClock(long clock,int offset) {
      int days = (int)(clock / SECSPERDAY);
      int tm_secs = (int)(clock % SECSPERDAY);
      tm_secs += offset;
      while (tm_secs < 0) {
	tm_secs += SECSPERDAY;
	--days;
      }
      while (tm_secs >= SECSPERDAY) {
	tm_secs -= SECSPERDAY;
	++days;
      }
      
      setSecs(tm_secs);
      
      int doc = days + DAYSADJ;
      tm_wday = (CENT_WDAY + doc) % DAYSPERWEEK;

      // now compute date from days since EPOCH
      int leapyear = 2;		/* not leapyear adj = 2 */
      // 1461 days in 4 years
      // FIXME: use code from JulianDate.java for extended range.
      tm_year = (doc - doc/1461 +364)/365;	/* calculate year */
      tm_yday = doc - ((tm_year-1)*1461)/4;	/* day of year conversion */
      if (tm_year % 4 == 0)			/* is this a leapyear? */
	leapyear = 1;				/* yes - reset adj to 1 */
      if (tm_yday > 59 && (tm_yday > 60 || leapyear == 2))
	tm_yday += leapyear;			/* correct for leapyear */

      tm_mon = (269 + tm_yday * 9) / 275;		/* calculate month */
      tm_mday = tm_yday + 30 - 275 * tm_mon/9;	/* calc day of month */
      --tm_mon;	// unix convention
    }
  }

  /** Compute UT from clock.  This does not include leap second corrections.
      @param clock	seconds since 1970
      @return a new tm object with all time fields computed.
   */
  public tm gmtime(long clock) {
    tm t = new tm();
    t.setClock(clock,0);
    t.tm_zone = "GMT";
    return t;
  }

  /** Compute UTC from clock.  This includes leap second corrections if
      compiled into the current timezone file.
      @param clock	seconds since 1970
      @return a new tm object with all time fields computed.
   */
  public tm utctime(long clock) {
    tm t = new tm();
    timesub(clock,null,t);
    return t;
  }

  /** Compute local time from seconds since the epoch, storing into
      an existing tm object.
      @param clock	seconds since 1970
      @param t	a tm object to store the computed time fields
      @return the offset of the localtime from UT
   */
  public int localtime(long clock,tm t) {
    return timesub(clock,getTZ(clock),t);
  }
    
  /** Lookup which timezone a given instant should use.  */
  private TZType getTZ(long clock) {
    // FIXME: use binary search
    if (transTimes.length > 0 && clock >= transTimes[0]) {
      int i = 1;
      for (;i < transTimes.length; ++i)
        if (clock < transTimes[i]) break;
      return this.tz[transTypes[i - 1]];
    }
    return normaltz;
  }

  /** Compute local time from seconds since the epoch.
      @param clock	seconds since 1970
   */
  public tm localtime(long clock) {
    tm t = new tm();
    localtime(clock,t);
    return t;
  }

  /** Calculate seconds since the epoch, the reverse of localtime().  
  Unused fields are computed and stored in <code>yourtm</code>.
  @param yourtm The tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec fields are used
  	and validated.  Other fields are computed.
  @throws IllegalArgumentException If used fields are invalid.
  @return seconds since the epoch.
   */
  public long mktime(tm yourtm) {
    return mktime(yourtm,false);
  }

  private long mktime(tm yourtm,boolean raw) {
    int t = 0;
    int bits = 31;
    int offset = getRawOffset() / 1000;
    tm mytm = new tm();
    // use binary search
    // FIXME: make smarter initial guess?
    for (;;) {
      if (raw)
        //timesub(t,tz,mytm);
	mytm.setClock(t,offset);
      else
	localtime(t,mytm);
      int direction = mytm.compareTo(yourtm);
      if (direction == 0) {
        yourtm.tm_wday = mytm.tm_wday;
        yourtm.tm_yday = mytm.tm_yday;
        yourtm.tm_isdst = mytm.tm_isdst;
        yourtm.tm_zone = mytm.tm_zone;
        return t;
      }
      //System.err.println(mytm.toString() + ", " + t + ", " + direction);
      if (bits-- < 0)
        throw new IllegalArgumentException("bad time: " + yourtm);
      if (bits < 0)
	--t;
      else if (direction > 0)
	t -=  1 << bits;
      else	
        t +=  1 << bits;
    }
  }

  /** Compute tm variables from clock with leapsecond correction.
      @param clock	Seconds since 1970
      @param tz		timezone 
      @param t		localtime variables to set
      @return	The offset from GMT including timezone, DST, and leap seconds.
   */
  private int timesub(long clock, TZType tz, tm t) {
    boolean		hit = false;
    int offset = (tz == null) ? 0 : tz.offset;

    for (int y = leapSecs.length; (y-=2) >= 0; ) {
      int ls_trans = leapSecs[y];
      int ls_corr = leapSecs[y+1];
      if (clock >= ls_trans) {
	if (clock == ls_trans)
	  hit = ((y == 0 && ls_corr > 0) || ls_corr > leapSecs[y-1]);
	offset -= ls_corr;
	break;
      }
    }

    t.setClock(clock,offset);

    // A positive leap second requires a special
    // representation.  This uses "... ??:59:60".
    if (hit) t.tm_sec += 1;

    if (tz != null) {
      t.tm_isdst = tz.isdst;
      t.tm_zone = tz.name;
    }
    else {
      t.tm_isdst = false;
      t.tm_zone = "UTC";
    }
    return offset;
  }

  public static void main(String[] argv) throws Exception {
    ZoneInfo tz = new ZoneInfo("EST5EDT");
    int now = (int)(System.currentTimeMillis() / 1000);
    System.err.println("Now = " + tz.localtime(now));
    Calendar cal = new GregorianCalendar();
    cal.setTimeZone(tz);
    cal.setTime(new Date());
    System.err.println("Now = " + cal);
  }

  /** Test the class by printing corresponding GMT and localized
      GregorianCalendar times before and after each timezone and 
      leapsecond transition, and at the minimum and maximum unix
      format times. */
  static class TZDump {
    private String zone;
    private ZoneInfo tz;
    private Calendar cal = new GregorianCalendar();
    private DateFormat fmt = DateFormat.getDateTimeInstance(
      DateFormat.LONG,DateFormat.LONG);

    private TZDump(String zone) throws IOException {
      if (zone != null)
	tz = new ZoneInfo(zone);
      else {
	tz = new ZoneInfo();
	zone = "localtime";
      }
      this.zone = zone;
      cal.setTimeZone(tz);
      fmt.setCalendar(cal);
    }
    private String dumplcl(int time) {
      //tm t = tz.localtime(time);
      //return t.toString() + " isdst=" + t.tm_isdst;
      return fmt.format(new Date(time * 1000L));
    }
    private void dump(int time) {
      tm t = tz.localtime(time);
      System.out.println(zone + ' ' + tz.gmtime(time) + " = " + dumplcl(time));
    }
    /** Dump daylight savings time transitions. */
    private void dumpdst() {
      for (int i = 0; i < tz.transTimes.length; ++i) {
        int t = tz.transTimes[i];
	dump(t-1);
	dump(t);
      }
    }
    /** Dump leapseconds. */
    private void dumpleap() {
      for (int i = 0; i < tz.leapSecs.length; i += 2) {
        int t = tz.leapSecs[i];
	dump(t-1);
	dump(t);
	dump(t+1);
      }
    }

    private static int now = (int)(System.currentTimeMillis() / 1000);

    private static void dumpzone(String tzname) throws IOException {
      TZDump tz = new TZDump(tzname);
      System.out.println(tz.dumplcl(now));
      tz.dump(Integer.MIN_VALUE);
      tz.dumpdst();
      tz.dumpleap();
      tz.dump(Integer.MAX_VALUE);
    }

    /** Dump DST and leapsecond transitions for each timezone
        on the command line. */
    public static void main(String[] argv) throws Exception {
      if (argv.length == 0)
        dumpzone(null);
      else
	for (int i = 0; i < argv.length; ++i)
	  dumpzone(argv[i]);
    }
  }

}
