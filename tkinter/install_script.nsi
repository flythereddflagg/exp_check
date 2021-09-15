# define installer name
!define APP_NAME "Exp Check"
OutFile "exp_check_installer.exe"
 
# set desktop as install directory
InstallDir $PROFILE\.exp_check
 
# default section start
Section
    CreateDirectory $INSTDIR
    # define output path
    SetOutPath $INSTDIR
     
    # specify file to go in output path
    File /r .\dist\*
    
    # make shortcuts: first two for the start menu
    CreateDirectory "$SMPROGRAMS\${APP_NAME}"
    
    CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${APP_NAME}\${APP_NAME}.exe" "" "$INSTDIR\${APP_NAME}\data\exp_check.ico"
    CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME} - Date Checker.lnk" "$INSTDIR\${APP_NAME}\${APP_NAME}.exe" "-chk" "$INSTDIR\${APP_NAME}\data\exp_check.ico"
    
    # and one for the startup menu
    CreateShortCut "$SMPROGRAMS\Startup\${APP_NAME} - Date Checker.lnk" "$INSTDIR\${APP_NAME}\${APP_NAME}.exe" "-chk" "$INSTDIR\${APP_NAME}\data\exp_check.ico"
    
    # define uninstaller name
    WriteUninstaller $INSTDIR\uninstaller.exe
     
     
    #-------
    # default section end
SectionEnd
 
# create a section to define what the uninstaller does.
# the section will always be named "Uninstall"
Section "Uninstall"
 
# Always delete uninstaller first
Delete $INSTDIR\uninstaller.exe
Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME} - Date Checker.lnk"
Delete "$SMPROGRAMS\Startup\${APP_NAME} - Date Checker.lnk"
RMDir "$SMPROGRAMS\${APP_NAME}"
RMDir /r "$INSTDIR\Exp Check"
RMDir $INSTDIR
 
SectionEnd