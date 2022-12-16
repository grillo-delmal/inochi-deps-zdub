%global debug_package %{nil}

%define lib_name      eventcore
%define lib_ver       0.9.21
%define lib_gitver    0.9.21
%define lib_semver    0.9.21
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
URL:            https://github.com/vibe-d/eventcore
Source0:        https://github.com/vibe-d/eventcore/archive/refs/tags/v%{lib_gitver}/eventcore-%{lib_gitver}.tar.gz

BuildRequires:  setgittag
BuildRequires:  git
BuildRequires:  ldc
BuildRequires:  dub
BuildRequires:  zdub-taggedalgebraic-static


%description
An actual description of %{lib_name}
#FIXME: generate an actual description


%package devel
Provides:       %{name}-static = %{version}-%{release}
Summary:        Support to use %{lib_name} for developing D applications
Group:          Development/Libraries

Requires:       zdub-dub-settings-hack


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_gitver} -p1
setgittag --rm -f -m v%{lib_gitver}

mv LICENSE.txt LICENSE

#FIXME: libasync is not packaged
mkdir -p libasync
echo "name \"libasync\"" > libasync/dub.sdl
pushd libasync
setgittag -m --rm -f v0.8.2
popd

mkdir -p /builddir/.dub/packages/libasync-0.8.2
mv ./libasync /builddir/.dub/packages/libasync-0.8.2/libasync


%build
dub build


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}
mkdir -p %{buildroot}%{_includedir}/zdub/libasync-0.8.2
cp -r /builddir/.dub/packages/libasync-0.8.2/libasync %{buildroot}%{_includedir}/zdub/libasync-0.8.2/libasync


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/
%{_includedir}/zdub/libasync-0.8.2/


%changelog
%autochangelog
