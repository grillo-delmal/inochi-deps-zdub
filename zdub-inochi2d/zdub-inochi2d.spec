%global debug_package %{nil}

%define lib_name      inochi2d
%define lib_ver       0.8.3
%define lib_gitver    0.8.3
%define lib_semver    0.8.3
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
License:        BSD-2-Clause
URL:            https://github.com/Inochi2D/%{lib_name}
Source0:        https://github.com/Inochi2D/inochi2d/archive/%{inochi2d_commit}/inochi2d-%{inochi2d_short}.tar.gz

Patch0:         inochi2d_0.8.0_no-gitver.patch

BuildRequires:  setgittag
BuildRequires:  git
BuildRequires:  ldc
BuildRequires:  dub
BuildRequires:  zdub-fghj-static
BuildRequires:  zdub-i2d-opengl-static
BuildRequires:  zdub-imagefmt-static
BuildRequires:  zdub-inmath-static
BuildRequires:  zdub-silly-static


%description
An actual description of %{lib_name}
#FIXME: generate an actual description


%package devel
Provides:       %{name}-static = %{version}-%{release}
Summary:        Support to use %{lib_name} for developing D applications
Group:          Development/Libraries

Requires:       zdub-dub-settings-hack
Requires:       zdub-fghj-static
Requires:       zdub-i2d-opengl-static
Requires:       zdub-imagefmt-static
Requires:       zdub-inmath-static
Requires:       zdub-silly-static


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_gitver} -p1
setgittag --rm -f -m v%{lib_gitver}

# FIX: Inochi2D version dependent on git
cat > source/inochi2d/ver.d <<EOF
module inochi2d.ver;

enum IN_VERSION = "%{inochi2d_semver}";
EOF


%check
dub build
dub clean


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/


%changelog
%autochangelog
