{
  'targets': [
    {
      'target_name': 'node-icu-tokenizer',
      'sources': [ 'node-icu-tokenizer.cpp' ],
      'cflags_cc': [
        '-std=c++0x',
        '-fexceptions',
        '-Wall',
        '-O3'
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
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
           'conditions': [
          ['node_with_ltcg=="true"', {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'WholeProgramOptimization': 'true' # /GL, whole program optimization, needed for LTCG
              },
              'VCLibrarianTool': {
                'AdditionalOptions': [
                  '/LTCG:INCREMENTAL', # incremental link-time code generation
                ]
              },
              'VCLinkerTool': {
                'OptimizeReferences': 2, # /OPT:REF
                'EnableCOMDATFolding': 2, # /OPT:ICF
                'LinkIncremental': 1, # disable incremental linking
                'AdditionalOptions': [
                  '/LTCG:INCREMENTAL', # incremental link-time code generation
                ]
              }
            }
          }]
        ],
         'defines': [
          'NAPI_DISABLE_CPP_EXCEPTIONS', 
          'NAPI_VERSION=3',
          'VIPS_CPLUSPLUS_EXPORTS',
          '_ALLOW_KEYWORD_MACROS'
        ],
        'libraries': [
          '<(module_root_dir)/lib/icudt.lib', 
          '<(module_root_dir)/lib/icuin.lib', 
          '<(module_root_dir)/lib/icuio.lib', 
          '<(module_root_dir)/lib/icutest.lib', 
          '<(module_root_dir)/lib/icutu.lib', 
          '<(module_root_dir)/lib/icuuc.lib'
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
          '<(module_root_dir)/lib/libicudata.so', 
          '<(module_root_dir)/lib/libicui18n.so', 
          '<(module_root_dir)/lib/libicuio.so', 
          # '<(module_root_dir)/lib/libicule.so', 
          '<(module_root_dir)/lib/libiculx.so', 
          '<(module_root_dir)/lib/libicutu.so', 
          '<(module_root_dir)/lib/libicuuc.so',
          '-Wl,-s -Wl,--disable-new-dtags -Wl,-rpath=\'$${ORIGIN}/../../lib/\''
        ],
      }],
      ['OS=="mac"', {
          'libraries': [ 
            '<(module_root_dir)/lib/libicudata.so', 
            '<(module_root_dir)/lib/libicui18n.so', 
            '<(module_root_dir)/lib/libicuio.so', 
            '<(module_root_dir)/lib/libicule.so', 
            '<(module_root_dir)/lib/libiculx.so', 
            '<(module_root_dir)/lib/libicutu.so', 
            '<(module_root_dir)/lib/libicuuc.so'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
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
                'ExceptionHandling': 1,
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
