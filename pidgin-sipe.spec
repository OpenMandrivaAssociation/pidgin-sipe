%define __libtoolize /bin/true

Name: 		pidgin-sipe
Version: 	1.15.0
Release: 	1
URL: 		http://sipe.sourceforge.net/
License: 	GPLv2+
Group: 		Networking/Instant messaging
Source0: 	http://downloads.sourceforge.net/project/sipe/sipe/%{name}-%{version}/%{name}-%{version}.tar.bz2
Summary: 	Pidgin protocol (SIP/SIMPLE) plugin to connect to MS Office Communicator
#BuildRequires:	pidgin-devel
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	gmime-devel
BuildRequires:	gettext
BuildRequires:	krb5-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	intltool
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libnice-devel >= 0.1.0
BuildRequires:	pkgconfig(nss)

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
sed -i 's/-Werror//g' configure.ac configure

%configure --with-krb5 --disable-purple --enable-telepathy
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
#%{_libdir}/purple-2/*.so
%{_libdir}/telepathy-sipe
%{_datadir}/telepathy/profiles/sipe.profile
%{_datadir}/empathy/icons/hicolor/*/apps/im-sipe.*
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sipe.service
