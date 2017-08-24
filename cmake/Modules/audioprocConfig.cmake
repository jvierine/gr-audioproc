INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_AUDIOPROC audioproc)

FIND_PATH(
    AUDIOPROC_INCLUDE_DIRS
    NAMES audioproc/api.h
    HINTS $ENV{AUDIOPROC_DIR}/include
        ${PC_AUDIOPROC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    AUDIOPROC_LIBRARIES
    NAMES gnuradio-audioproc
    HINTS $ENV{AUDIOPROC_DIR}/lib
        ${PC_AUDIOPROC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(AUDIOPROC DEFAULT_MSG AUDIOPROC_LIBRARIES AUDIOPROC_INCLUDE_DIRS)
MARK_AS_ADVANCED(AUDIOPROC_LIBRARIES AUDIOPROC_INCLUDE_DIRS)

