%global debug_package %{nil}

%define lib_name      vmc-d
%define lib_ver       1.1.2
%define lib_gitver    1.1.2
%define lib_semver    1.1.2
%define lib_dist      0
%define lib_commit    b32fb96b4ce9a6357b193fb297e44edd8e6112ed
%define lib_short     b32fb96

%if 0%{lib_dist} > 0
%define lib_suffix ^%{lib_dist}.git%{lib_short}
%endif

Name:           zdub-%{lib_name}
Version:        %{lib_ver}%{?lib_suffix:}
Release:        %autorelease
Summary:        %{lib_name} library for D
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/Inochi2D/%{lib_name}
Source0:        https://github.com/Inochi2D/%{lib_name}/archive/v%{lib_gitver}/%{lib_name}-%{lib_gitver}.tar.gz

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


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_gitver} -p1
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
