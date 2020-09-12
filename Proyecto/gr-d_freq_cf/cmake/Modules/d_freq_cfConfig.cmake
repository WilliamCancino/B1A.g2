INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_D_FREQ_CF d_freq_cf)

FIND_PATH(
    D_FREQ_CF_INCLUDE_DIRS
    NAMES d_freq_cf/api.h
    HINTS $ENV{D_FREQ_CF_DIR}/include
        ${PC_D_FREQ_CF_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    D_FREQ_CF_LIBRARIES
    NAMES gnuradio-d_freq_cf
    HINTS $ENV{D_FREQ_CF_DIR}/lib
        ${PC_D_FREQ_CF_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/d_freq_cfTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(D_FREQ_CF DEFAULT_MSG D_FREQ_CF_LIBRARIES D_FREQ_CF_INCLUDE_DIRS)
MARK_AS_ADVANCED(D_FREQ_CF_LIBRARIES D_FREQ_CF_INCLUDE_DIRS)
