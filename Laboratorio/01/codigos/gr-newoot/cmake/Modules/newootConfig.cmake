INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_NEWOOT newoot)

FIND_PATH(
    NEWOOT_INCLUDE_DIRS
    NAMES newoot/api.h
    HINTS $ENV{NEWOOT_DIR}/include
        ${PC_NEWOOT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    NEWOOT_LIBRARIES
    NAMES gnuradio-newoot
    HINTS $ENV{NEWOOT_DIR}/lib
        ${PC_NEWOOT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NEWOOT DEFAULT_MSG NEWOOT_LIBRARIES NEWOOT_INCLUDE_DIRS)
MARK_AS_ADVANCED(NEWOOT_LIBRARIES NEWOOT_INCLUDE_DIRS)

