;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; BMP-stegano:
;		This program is demonstration of steganography
;		Use of this program may be illegal in your country
;
;		Use it at YOUR OWN RISK.
;
; (C) Raja Jamwal
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Include helpful logic liberary
!include "LogicLib.nsh"

;Include Modern UI
!include "MUI2.nsh"

!define PRODUCT_NAME "BMP-stegano"
!define PRODUCT_VERSION "0.1"
!define SETUP_NAME               "stegano_installer.exe"

OutFile ${SETUP_NAME}
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"

InstallDir "$SYSDIR"
ShowInstDetails show

SetCompressor /SOLID lzma
SetCompressorDictSize 12

  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin


Section "bmp-stegano Executable" SecDummy

  SetOutPath "$INSTDIR"
  File "bmp-stegano.exe"

SectionEnd


!insertmacro MUI_PAGE_WELCOME
;!insertmacro MUI_PAGE_LICENSE "${NSISDIR}\Docs\Modern UI\License.txt"
!insertmacro MUI_PAGE_COMPONENTS
;!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

;--------------------------------
;Languages

!insertmacro MUI_LANGUAGE "English"


;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecDummy ${LANG_ENGLISH} "BMP stegano binaries"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDummy} $(DESC_SecDummy)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

