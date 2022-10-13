%global debug_package %{nil}

%define lib_name      dportals
%define lib_ver       0.1.0
%define lib_gitver    0.1.0
%define lib_semver    0.1.0
%define lib_dist      0
%define lib_commit    52e805408bc43c2f74a480e16e17d8d58682fd1f
%define lib_short     52e8054

%if 0%{lib_dist} > 0
%define lib_suffix ^%{lib_dist}.git%{lib_short}
%endif

Name:           zdub-%{lib_name}
Version:        %{lib_ver}%{?lib_suffix:}
Release:        %autorelease
Summary:        xdg-portals for D
Group:          Development/Libraries
License:        BSD-2-Clause
URL:            https://github.com/Inochi2D/%{lib_name}
Source0:        https://github.com/Inochi2D/%{lib_name}/archive/v%{lib_gitver}/%{lib_name}-%{lib_gitver}.tar.gz
Source1:        LICENSE

BuildRequires:  setgittag
BuildRequires:  git


%description
This D library allows you to interface with
XDG Desktop Portals when you aren't using GTK or Qt.


%package devel
Provides:       %{name}-static = %{version}-%{release}
Summary:        Support to use %{lib_name} for developing D applications
Group:          Development/Libraries

Requires:       ldc
Requires:       dub

Requires:       zdub-dub-settings-hack
Requires:       zdub-ddbus-static
Requires:       zdub-silly-static


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_gitver} -p1
setgittag --rm -f -m v%{lib_gitver}

cp %{SOURCE1} .


%build


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/


%changelog
%autochangelog
