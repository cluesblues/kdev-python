cmake_minimum_required(VERSION 3.0)
project(kdevpython VERSION 5.6.40)

# KDevplatform dependency version
set(KDEVPLATFORM_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

find_package (ECM "5.28.0" REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${kdevpython_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH})

include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)

include(GenerateExportHeader)

include(ECMAddTests)
include(ECMSetupVersion)
include(ECMQtDeclareLoggingCategory)

if(POLICY CMP0071)
    # Avoids compat messages from CMake 3.10+, with Qt < 5.9.4
    # See https://bugreports.qt.io/browse/QTBUG-63442
    cmake_policy(SET CMP0071 OLD)
endif()

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wdocumentation")
endif()

add_definitions( -DTRANSLATION_DOMAIN=\"kdevpython\" )

# CMake looks for exactly the specified version first and ignores newer versions.
# To avoid that, start looking for the newest supported version and work down.
set(Python_ADDITIONAL_VERSIONS 3.9 3.8 3.7 3.6 3.5 3.4)
foreach(_PYTHON_V ${Python_ADDITIONAL_VERSIONS})
    find_package(PythonInterp ${_PYTHON_V})
    if ( PYTHONINTERP_FOUND )
        break()
    endif()
endforeach()
# Must unset before searching for libs, otherwise these are checked before the required version...
unset(Python_ADDITIONAL_VERSIONS)

if ( PYTHONINTERP_FOUND AND PYTHON_VERSION_STRING VERSION_GREATER "3.4" )
    # Find libraries that match the found interpreter (mismatched versions not supported).
    # This assumes libs are available for the newest Python version on the system.
    # KDevelop should _always_ be built against the newest possible version, so notabug.
    find_package(PythonLibs "${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}" REQUIRED EXACT)
endif()

if ( NOT PYTHONLIBS_FOUND OR PYTHONLIBS_VERSION_STRING VERSION_LESS "3.4.3" )
    message(FATAL_ERROR "Python >= 3.4.3 but < 3.10 with --enable-shared is required to build kdev-python")
endif()

configure_file(kdevpythonversion.h.cmake "${CMAKE_CURRENT_BINARY_DIR}/kdevpythonversion.h" @ONLY)

set(QT_MIN_VERSION "5.7.0")
find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED Core Widgets Test)
set(KF5_DEP_VERSION "5.28.0")
find_package(KF5 ${KF5_DEP_VERSION} REQUIRED
    I18n
    ThreadWeaver
    TextEditor
)
find_package(KDevPlatform ${KDEVPLATFORM_VERSION} CONFIG REQUIRED)
find_package(KDevelop ${KDEVPLATFORM_VERSION} REQUIRED)

if(NOT CMAKE_VERSION VERSION_LESS "3.10.0" AND KF5_VERSION VERSION_LESS "5.42.0")
    # Avoids bogus warnings with CMake 3.10+, KF5.42+ has workaround
    list(APPEND CMAKE_AUTOMOC_MACRO_NAMES "K_PLUGIN_FACTORY_WITH_JSON")
endif()

if ( NOT WIN32 )
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wfatal-errors -Wall")
endif ( NOT WIN32 )

# then, build the plugin
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/duchain
    ${CMAKE_CURRENT_SOURCE_DIR}/parser
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_subdirectory(app_templates)
add_subdirectory(parser)
add_subdirectory(duchain)
add_subdirectory(codecompletion)
add_subdirectory(debugger)
add_subdirectory(docfilekcm)

set(kdevpythonlanguagesupport_PART_SRCS
    codegen/correctionfilegenerator.cpp
    codegen/refactoring.cpp
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp
    pythonstylechecking.cpp

    # config pages:
    docfilekcm/docfilewizard.cpp
    docfilekcm/docfilemanagerwidget.cpp
    docfilekcm/kcm_docfiles.cpp
    pep8kcm/kcm_pep8.cpp
    projectconfig/projectconfigpage.cpp
)
ecm_qt_declare_logging_category(kdevpythonlanguagesupport_PART_SRCS
    HEADER codegendebug.h
    IDENTIFIER KDEV_PYTHON_CODEGEN
    CATEGORY_NAME "kdevelop.plugins.python.codegen"
)
ecm_qt_declare_logging_category(kdevpythonlanguagesupport_PART_SRCS
    HEADER pythondebug.h
    IDENTIFIER KDEV_PYTHON
    CATEGORY_NAME "kdevelop.plugins.python"
)

ki18n_wrap_ui(kdevpythonlanguagesupport_PART_SRCS
    codegen/correctionwidget.ui
    projectconfig/projectconfig.ui
    pep8kcm/pep8.ui
)

kdevplatform_add_plugin(kdevpythonlanguagesupport JSON kdevpythonsupport.json SOURCES ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    KDev::Interfaces
    KDev::Language
    KDev::Util
    KF5::ThreadWeaver
    KF5::TextEditor
    kdevpythoncompletion
    kdevpythonparser
    kdevpythonduchain
)

get_target_property(DEFINESANDINCLUDES_INCLUDE_DIRS KDev::DefinesAndIncludesManager INTERFACE_INCLUDE_DIRECTORIES)
include_directories(${DEFINESANDINCLUDES_INCLUDE_DIRS})

install(DIRECTORY documentation_files DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)
install(DIRECTORY correction_files DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)
install(FILES codestyle.py DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)

install(FILES org.kde.kdev-python.metainfo.xml DESTINATION ${KDE_INSTALL_METAINFODIR})

# kdebugsettings file
# kdebugsettings >= 18.12 supports/pushes for some newer, not backward-compatible format.
# For ECM >= 5.59 we install categories files to new location, which is only supported by
# newer kdebugsettings also supporting the new content format, so we use that as base.
if (ECM_VERSION VERSION_GREATER "5.58.0")
    install(FILES kdevpythonsupport-newformat.categories RENAME kdevpythonsupport.categories
        DESTINATION ${KDE_INSTALL_LOGGINGCATEGORIESDIR}
    )
else()
    install(FILES kdevpythonsupport-oldformat.categories RENAME kdevpythonsupport.categories
        DESTINATION ${KDE_INSTALL_CONFDIR})
endif()

ki18n_install(po)

feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)
