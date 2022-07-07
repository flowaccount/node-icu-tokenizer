{
  'targets': [
    {
      'target_name': 'node-icu-tokenizer',
      'sources': [ 'node-icu-tokenizer.cpp' ],
      'cflags_cc': [
        '-std=c++17',
        '-fexceptions',
        '-Wall',
        '-O3'
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++17',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'OTHER_CPLUSPLUSFLAGS': [
          '-fexceptions',
          '-Wall',
          '-O3'
        ]
      },
      'defines': [ 'NAPI_VERSION=3' ],
      'dependencies': [
        '<!(node -p "require(\'node-addon-api\').gyp")'
      ],
      'include_dirs': [
          "./includes/",
          "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'conditions': [
        ['OS == "win"', {
         'defines': [
          'NAPI_DISABLE_CPP_EXCEPTIONS', 
          'NAPI_VERSION=3',
          'VIPS_CPLUSPLUS_EXPORTS',
          '_ALLOW_KEYWORD_MACROS',
          '_FILE_OFFSET_BITS=64'
        ],
        'libraries': [
          '<(module_root_dir)/lib/windows/icudt.lib', 
          '<(module_root_dir)/lib/windows/icuin.lib', 
          '<(module_root_dir)/lib/windows/icuio.lib', 
          '<(module_root_dir)/lib/windows/icutest.lib', 
          '<(module_root_dir)/lib/windows/icutu.lib', 
          '<(module_root_dir)/lib/windows/icuuc.lib',
        ],
       
        'msvs_disabled_warnings': [
          4275
        ]
      }],
      ['OS == "linux"', {
        'defines': [
              '_GLIBCXX_USE_CXX11_ABI=0'
         ],
        'libraries': [
          '<(module_root_dir)/lib/linux/libicudata.so.71',
          '<(module_root_dir)/lib/linux/libicui18n.so.71', 
          '<(module_root_dir)/lib/linux/libicuio.so.71', 
          '<(module_root_dir)/lib/linux/libicutest.so.71',
          '<(module_root_dir)/lib/linux/libicutu.so.71',
          '<(module_root_dir)/lib/linux/libicuuc.so.71',
          '-Wl,-s -Wl,--disable-new-dtags -Wl,-rpath=\'$${ORIGIN}/../../lib/linux\''
        ],
      }],
      ['OS=="mac"', {
      "libraries": ["<!@(icu-config --ldflags)"],
      "cflags": ["<!(icu-config --cppflags)"],
      "xcode_settings": {
        "OTHER_CFLAGS": [
          "<!(icu-config --cppflags)",
        ],
      },
        }]
      ],
      'configurations': {
      'Release': {
        'conditions': [
          ['OS == "linux"', {
            'cflags_cc': [
              '-Wno-cast-function-type'
            ]
          }],
          ['target_arch == "arm"', {
            'cflags_cc': [
              '-Wno-psabi'
            ]
          }],
          ['OS == "win"', {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'DebugInformationFormat': 3, # Generate a PDB
                'WarningLevel': 3,
                'BufferSecurityCheck': 'true',
                'ExceptionHandling': 1, # /EHsc
                'SuppressStartupBanner': 'true',
                'WarnAsError': 'false',
                'RuntimeLibrary': '2',
                'WholeProgramOptimization': 'true'
              },
              'VCLibrarianTool': {
                'AdditionalOptions': [
                  '/LTCG:INCREMENTAL'
                ]
              },
              'VCLinkerTool': {
                'ImageHasSafeExceptionHandlers': 'false',
                'OptimizeReferences': 2,
                'EnableCOMDATFolding': 2,
                'LinkIncremental': 1,
                'GenerateDebugInformation': 'true',
                'AdditionalOptions': [
                  '/LTCG:INCREMENTAL'
                ]
              }
            },
            'msvs_disabled_warnings': [
              4275
            ]
          }]
        ]
      }
    },
    }
  ]
}
