%global debug_package %{nil}

%define lib_name      bindbc-imgui
%define lib_ver       0.7.0
%define lib_gitver    0.7.0
%define lib_semver    0.7.0+build.22.gb3d6e32
%define lib_dist      22
%define lib_commit    b3d6e32cb0ce7c607a8e249a11c4a5a4ed0a19e8
%define lib_short     b3d6e32
%define cimgui_commit 49bb5ce65f7d5eeab7861d8ffd5aa2a58ca8f08c
%define cimgui_short  49bb5ce
%define imgui_commit  dd5b7c6847372016f45d5b5abda687bd5cd19224
%define imgui_short   dd5b7c6

%if 0%{lib_dist} > 0
%define lib_suffix ^%{lib_dist}.git%{lib_short}
%endif

Name:           zdub-%{lib_name}
Version:        %{lib_ver}%{?lib_suffix:}
Release:        %autorelease
Summary:        %{lib_name} library for D
Group:          Development/Libraries
License:        BSL-1.0 and MIT
URL:            https://github.com/Inochi2D/%{lib_name}
Source0:        https://github.com/Inochi2D/bindbc-imgui/archive/%{lib_commit}/bindbc-imgui-%{lib_short}.tar.gz
Source1:        https://github.com/Inochi2D/cimgui/archive/%{cimgui_commit}/cimgui-%{cimgui_short}.tar.gz
Source2:        https://github.com/Inochi2D/imgui/archive/%{imgui_commit}/imgui-%{imgui_short}.tar.gz

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
Requires:       zdub-bindbc-opengl-static
Requires:       zdub-bindbc-sdl-static

Requires:       cmake
Requires:       gcc
Requires:       gcc-c++
Requires:       freetype-devel
Requires:       SDL2-devel


%description devel
Sources to use the %{lib_name} library on dub using the
zdub-dub-settings-hack method.


%prep
%autosetup -n %{lib_name}-%{lib_commit} -p1
setgittag --rm -f -m v%{lib_gitver}

# cimgui
tar -xzf %{SOURCE1}
rm -rf deps/cimgui
mv cimgui-%{cimgui_commit} deps/cimgui

tar -xzf %{SOURCE2}
rm -rf deps/cimgui/imgui
mv imgui-%{imgui_commit} deps/cimgui/imgui

rm -rf deps/freetype
rm -rf deps/glbinding
rm -rf deps/glfw
rm -rf deps/SDL
rm -rf deps/cimgui/imgui/examples/

# FIX: Make bindbc-imgui submodule checking only check cimgui
rm -f .gitmodules
cat > .gitmodules <<EOF
[submodule "deps/cimgui"]
   path = deps/cimgui
   url = https://github.com/Inochi2D/cimgui.git
EOF
mkdir -p deps/cimgui/.git


%build


%install
mkdir -p %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}
cp -r . %{buildroot}%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}
# Dependency licenses
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}-devel/./deps/cimgui/
install -p -m 644 ./deps/cimgui/LICENSE \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}-devel/./deps/cimgui/LICENSE
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}-devel/./deps/imgui/
install -p -m 644 ./deps/cimgui/imgui/LICENSE.txt \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}-devel/./deps/imgui/LICENSE.txt


%files devel
%license LICENSE
%{_includedir}/zdub/%{lib_name}-%{lib_gitver}/%{lib_name}/
%{_datadir}/licenses/%{name}-devel/*


%changelog
%autochangelog
