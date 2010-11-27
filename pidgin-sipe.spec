Name: pidgin-sipe
Version: 1.11.2
Release: %mkrel 1
URL: http://sipe.sourceforge.net/
License: GPLv2
Group: Networking/Instant messaging
Source: http://downloads.sourceforge.net/project/sipe/sipe/pidgin-sipe-%{version}/pidgin-sipe-%{version}.tar.gz
Summary: SIP/SIMPLE plugin for pidgin
BuildRequires: pidgin-devel intltool libgstreamer-plugins-base-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
This project develops a third-party plugin for the Pidgin  multi-protocol
instant messenger. It implements the extended version of SIP/SIMPLE used by
various products:

    * Microsoft Office Communications Server (OCS 2007 and newer)
    * Microsoft Live Communications Server (LCS 2003/2005)
    * Reuters Messaging

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

%prep
%setup -q

%build
%configure2_5x --enable-telepathy=no
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/purple-2/*.la

%find_lang pidgin-sipe

%clean
rm -Rf %{buildroot}

%files -f pidgin-sipe.lang
%defattr(-,root,root)
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/sipe.png
%{_datadir}/pixmaps/pidgin/protocols/*/sipe.svg
