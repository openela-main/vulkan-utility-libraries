%global debug_package %{nil}

Name:           vulkan-utility-libraries
Version:        1.4.304.0
Release:        1%{?dist}
Summary:        Vulkan utility libraries

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source0:        %url/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Utility-Libraries-sdk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       vulkan-headers
Obsoletes:      vulkan-validation-layers-devel < 1.3.268.0-2
Provides:       vulkan-validation-layers-devel = %{version}-%{release}
Provides:       vulkan-validation-layers-devel%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep
%autosetup -p1 -n Vulkan-Utility-Libraries-vulkan-sdk-%{version}

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DBUILD_TESTS:BOOL=OFF \
        -DVUL_WERROR:BOOL=OFF \
        -DUPDATE_DEPS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a

%changelog
* Mon Jan 20 2025 José Expósito <jexposit@redhat.com> - 1.4.304.0-1
- Update to 1.4.304.0 SDK

* Tue May 28 2024 José Expósito <jexposit@redhat.com> - 1.3.283.0-1
- Update to 1.3.283.0 SDK

* Wed Jan 24 2024 José Expósito <jexposit@redhat.com> - 1.3.268.0-4
- Move Provides and Obsoletes to the devel package section

* Tue Jan 23 2024 José Expósito <jexposit@redhat.com> - 1.3.268.0-3
- Add Provides and Obsoletes vulkan-validation-layers-devel

* Mon Dec 11 2023 José Expósito <jexposit@redhat.com> - 1.3.268.0-2
- Remove unwanted Requires: vulkan-utility-libraries

* Fri Nov 10 2023 José Expósito <jexposit@redhat.com> - 1.3.268.0-1
- vulkan-utility-libraries 1.3.268.0
