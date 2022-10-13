%global debug_package %{nil}

%define lib_name      i18n-d
%define lib_ver       1.0.1
%define lib_gitver    1.0.1
%define lib_semver    1.0.1+build.2.g75c57ea
%define lib_dist      2
%define lib_commit    75c57ea0889d459b73765d932aec02f9b3e71b80
%define lib_short     75c57ea

%if 0%{lib_dist} > 0
%define lib_suffix ^%{lib_dist}.git%{lib_short}
%endif

Name:           zdub-%{lib_name}
Version:        %{lib_ver}%{?lib_suffix:}
Release:        %autorelease
Summary:        %{lib_name} library for D
Group:          Development/Libraries
License:        BSD-2-Clause
URL:            https://github.com/KitsunebiGames/i18n
Source0:        https://github.com/KitsunebiGames/i18n/archive/%{lib_commit}/i18n-%{lib_short}.tar.gz

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
Requires:       zdub-silly-static


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n i18n-%{lib_commit} -p1
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
