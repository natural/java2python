@IF EXIST "%~dp0\python.exe" (
  "%~dp0\python.exe"  "%~dp0\j2py" %*
) ELSE (
  @SETLOCAL
  @SET PATHEXT=%PATHEXT:;.PY;=;%
  python "%~dp0\j2py" %*
)