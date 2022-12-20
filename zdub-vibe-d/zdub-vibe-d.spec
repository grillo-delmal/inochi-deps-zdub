%global debug_package %{nil}

%define lib_name      vibe-d
%define lib_ver       0.9.5
%define lib_gitver    0.9.5
%define lib_semver    0.9.5
%define lib_dist      0
%define lib_commit    0000000
%define lib_short     0000000

%if 0%{lib_dist} > 0
%define lib_suffix ^%{lib_dist}.git%{lib_short}
%endif

Name:           zdub-%{lib_name}
Version:        %{lib_ver}%{?lib_suffix:}
Release:        %autorelease
Summary:        %{lib_name} library for D
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/vibe-d/vibe.d
Source0:        https://github.com/vibe-d/vibe.d/archive/refs/tags/v%{lib_gitver}/vibe-d-%{lib_gitver}.tar.gz

BuildRequires:  setgittag
BuildRequires:  git
BuildRequires:  ldc
BuildRequires:  dub
BuildRequires:  zdub-diet-ng-static
BuildRequires:  zdub-mir-linux-kernel-static
BuildRequires:  zdub-openssl-static
BuildRequires:  zdub-stdx-allocator-static
BuildRequires:  zdub-vibe-core-static


%description
An actual description of %{lib_name}
#FIXME: generate an actual description


%package devel
Provides:       %{name}-static = %{version}-%{release}
Summary:        Support to use %{lib_name} for developing D applications
Group:          Development/Libraries

Requires:       zdub-dub-settings-hack
Requires:       zdub-diet-ng-static
Requires:       zdub-mir-linux-kernel-static
Requires:       zdub-openssl-static
Requires:       zdub-stdx-allocator-static
Requires:       zdub-vibe-core-static


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n vibe.d-%{lib_gitver} -p1
setgittag --rm -f -m v%{lib_gitver}

mv LICENSE.txt LICENSE
rm -rf lib


%check
dub build --cache=local --temp-build

dub clean


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/


%changelog
%autochangelog
