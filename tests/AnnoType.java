@interface RequestForEnhancement {
    int    id();
    String synopsis();
    String engineer() default "[unassigned]";
    String date()    default "[unimplemented]";

}


@interface Copyright {
    String value();
}

@interface FancyDeco {
    int id();
    String key();
    String value() default "fancy decorated";
}

@interface Marker {}

interface PlaceHolder {
    int x = 3;
}


@Copyright("2008 Anonymous")
@Marker
@FancyDeco(id=PlaceHolder.x+
33, key="k", value="v")
public class AnnoType  {
}