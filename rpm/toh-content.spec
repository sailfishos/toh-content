Name:    toh-content
Version: 0.1.0
Release: 0
Summary: Official Jolla TOH content
License: BSD-3-Clause
URL:     https://github.com/sailfishos/toh-content
Source0: %{name}-%{version}.tar.bz2

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build here

%install
install -D -m0755 dist/change_ambience.sh %{buildroot}%{_libexecdir}/change_ambience.sh
install -D -m0644 overrides/inari_blue.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0004/inari_blue.yaml
install -D -m0644 overrides/kaamos_black.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0002/kaamos_black.yaml
install -D -m0644 overrides/snow_white.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0003/snow_white.yaml
install -D -m0644 overrides/the_orange.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0001/the_orange.yaml

%files
%license LICENSES/BSD-3-Clause.txt
%{_datadir}/tohd-1/tohs/0001
%{_libexecdir}/change_ambience.sh
