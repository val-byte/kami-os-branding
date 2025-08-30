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

mv logos/* %{buildroot}%{_datadir}/pixmaps

%files
%attr(0755,root,root) %{_datadir}/pixmaps/fedora*
%attr(0755,root,root) %{_datadir}/pixmaps/system-*
