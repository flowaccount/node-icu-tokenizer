{
  'targets': [
    {
      'target_name': 'node-icu-tokenizer',
      'sources': [ 'node-icu-tokenizer.cpp' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS', 'NAPI_VERSION=3' ],
      'dependencies': [
        '<!(node -p "require(\'node-addon-api\').gyp")'
      ],
      'include_dirs': [
          "./includes/",
          "./lib/",
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
          # '<(module_root_dir)/lib/icule.lib', 
          '<(module_root_dir)/lib/iculx.lib', 
          '<(module_root_dir)/lib/icutu.lib', 
          '<(module_root_dir)/lib/icuuc.lib'
        ],
       
        'msvs_disabled_warnings': [
          4275
        ]
      }],
      ['OS == "linux"', {
        'libraries': [ 
          '<(module_root_dir)/lib/libicudata.so.60', 
          '<(module_root_dir)/lib/libicui18n.so.60', 
          '<(module_root_dir)/lib/libicuio.so.60', 
          # '<(module_root_dir)/lib/libicule.so.60', 
          '<(module_root_dir)/lib/libiculx.so.60', 
          '<(module_root_dir)/lib/libicutu.so.60', 
          '<(module_root_dir)/lib/libicuuc.so.60',
          '-Wl,-s -Wl,--disable-new-dtags -Wl,-rpath=\'$${ORIGIN}/../../lib\''
        ],
      }],
      ['OS=="mac"', {
          'libraries': [ 
            '<(module_root_dir)/lib/libicudata.so.60', 
            '<(module_root_dir)/lib/libicui18n.so.60', 
            '<(module_root_dir)/lib/libicuio.so.60', 
            '<(module_root_dir)/lib/libicule.so.60', 
            '<(module_root_dir)/lib/libiculx.so.60', 
            '<(module_root_dir)/lib/libicutu.so.60', 
            '<(module_root_dir)/lib/libicuuc.so.60'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
    }
  ]
}
