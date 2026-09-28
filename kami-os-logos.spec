%global debug_package %{nil}
%global vendor val-byte

Name:           kami-os-logos
Version:        0.1
Release:        1%{?dist}
Summary:        kamios logos

License:        MIT
Provides: fedora-logos
Provides: centos-logos
Provides: system-logos
Obsoletes: fedora-logos
Obsoletes: centos-logos
Obsoletes: system-logos
URL:            https://github.com/val-byte/kami-os-branding
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
Logos for Kami-Os

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 %{buildroot}%{_datadir}/pixmaps
mkdir -p -m0755 %{buildroot}%{_datadir}/plymouth/themes/spinner

mv logos/* %{buildroot}%{_datadir}/pixmaps
mv plymouth/* %{buildroot}%{_datadir}/plymouth/themes/spinner
for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256; do
  mkdir -p -m0755 %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
  mv icons/hicolor/${size}/apps/fedora-logo-icon.png %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
done

%files
%attr(0755,root,root) %{_datadir}/pixmaps/fedora*
