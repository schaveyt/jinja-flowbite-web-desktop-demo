# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=({{APP_MAJOR_VERSION}}, {{APP_MINOR_VERSION}}, {{APP_PATCH_VERSION}}, 0),
    prodvers=({{APP_MAJOR_VERSION}}, {{APP_MINOR_VERSION}}, {{APP_PATCH_VERSION}}, 0),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    VarFileInfo([VarStruct('Translation', [0, 1200])]), 
    StringFileInfo(
      [
      StringTable(
        '000004b0',
        [StringStruct('Comments', 'my_app'),
        StringStruct('CompanyName', 'UNDEFINED'),
        StringStruct('FileDescription', 'my_app'),
        StringStruct('FileVersion', '{{SHORT_VERSION}}'),
        StringStruct('InternalName', 'my_app.exe'),
        StringStruct('LegalCopyright', 'Copyright © 2024 - 2024 UNDEFINED'),
        StringStruct('OriginalFilename', 'my_app.exe'),
        StringStruct('ProductName', 'my_app'),
        StringStruct('ProductVersion', '{{FULL_VERSION}}'),
        StringStruct('Assembly Version', '{{SHORT_VERSION}}')])
      ])
  ]
)