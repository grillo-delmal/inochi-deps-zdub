%global debug_package %{nil}

%define lib_name      inochi2d
%define lib_ver       0.7.2
%define lib_gitver    0.7.2
%define lib_semver    0.7.2+build.62.g08fe198
%define lib_dist      62
%define lib_commit    08fe19825b0db01c0a7831711722e5c9660d74ad
%define lib_short     08fe198

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
Source0:        https://github.com/Inochi2D/%{lib_name}/archive/%{lib_commit}/%{lib_name}-%{lib_short}.tar.gz

Patch0:         inochi2d_0.7.2_no-gitver.patch

BuildRequires:  setgittag
BuildRequires:  git


%description
An actual description of %{lib_name}
#FIXME: generate an actual description


%package devel
Provides:       %{name}-static = %{version}-%{release}
Summary:        Support to use %{lib_name} for developing D applications
Group:          Development/Libraries

Requires:       ldc
Requires:       dub

Requires:       zdub-dub-settings-hack
Requires:       zdub-imagefmt-static
Requires:       zdub-bindbc-opengl-static
Requires:       zdub-silly-static
Requires:       zdub-inmath-static
Requires:       zdub-fghj-static


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_commit} -p1
setgittag --rm -f -m v%{lib_gitver}


%build


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/


%changelog
%autochangelog
