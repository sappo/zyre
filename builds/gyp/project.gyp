################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
#   GYP file for zyre
#   gyp --depth=.
{
  'target_defaults': {
    'include_dirs': [
      '../../../libzmq/include',
      '../../../czmq/include',
      '../../include',
      '.'
    ],
    'defines': [
      'ZYRE_GYP_BUILD'
    ],
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'ZYRE_HAVE_WINDOWS',
          'ZMQ_STATIC',
          'CZMQ_STATIC',
          'ZYRE_STATIC'
        ],
        'libraries': [
          'ws2_32',
          'advapi32',
          'iphlpapi',
          'Rpcrt4'
        ]
      }],
      [ 'OS=="mac"', {
        'defines': [
          'ZYRE_HAVE_OSX'
        ]
      }],
      [ 'OS=="linux"', {
        'defines': [
          'ZYRE_HAVE_LINUX'
        ],
        'xcode_settings': {
          'OTHER_CFLAGS': [
            '-fPIC'
          ],
        },
        'libraries': [
          '-lpthread'
        ]
      }]
    ]
  },
  'targets': [
    {
      'target_name': 'libzyre',
      'type': 'static_library',
      'sources': [
        'platform.h',
        '../../include/zyre.h',
        '../../src/zre_msg.c',
        '../../src/zre_msg.h',
        '../../src/zyre.c',
        '../../include/zyre.h',
        '../../src/zyre_event.c',
        '../../include/zyre_event.h',
        '../../src/zyre_group.c',
        '../../src/zyre_group.h',
        '../../src/zyre_node.c',
        '../../src/zyre_node.h',
        '../../src/zyre_peer.c',
        '../../src/zyre_peer.h',
        '../../include/zyre_library.h',
        '../../src/zyre_selftest.c',
        '../../src/zyre_classes.h'
      ],
      'dependencies': [
        '../../../libzmq/builds/gyp/project.gyp:libzmq',
        '../../../czmq/builds/gyp/project.gyp:libczmq',
      ],
      'copies': [
        {
          'destination': '../../src',
          'files': [
              'platform.h'
          ]
        }
      ]
    },
    {
      'target_name': 'perf_local',
      'type': 'executable',
      'sources': [
        '../../src/perf_local.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    },
    {
      'target_name': 'perf_remote',
      'type': 'executable',
      'sources': [
        '../../src/perf_remote.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    },
    {
      'target_name': 'zpinger',
      'type': 'executable',
      'sources': [
        '../../src/zpinger.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    },
    {
      'target_name': 'ztester_beacon',
      'type': 'executable',
      'sources': [
        '../../src/ztester_beacon.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    },
    {
      'target_name': 'ztester_gossip',
      'type': 'executable',
      'sources': [
        '../../src/ztester_gossip.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    },
    {
      'target_name': 'zyre_selftest',
      'type': 'executable',
      'sources': [
        '../../src/zyre_selftest.c'
      ],
      'dependencies': [
        'libzyre'
      ]
    }
  ]
}
