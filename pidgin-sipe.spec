Name:		pidgin-sipe
Version:	1.23.2
Release:	1
Summary:	Pidgin protocol (SIP/SIMPLE) plugin to connect to MS Office Communicator
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://sipe.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/sipe/sipe/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(purple)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(nice) >= 0.1.0
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	pkgconfig(libgadu)

%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)
    * Reuters Messaging

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

%prep
%setup -q

%build
%configure2_5x \
	--with-krb5 \
	--enable-purple \
	--disable-telepathy
%make

%check
%__make check

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Pidgin doesn't have 24 or 32 pixel icons
rm -f \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/24/sipe.png \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/32/sipe.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%dir %{_libdir}/purple-2
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/
%{_datadir}/appdata/%{name}.metainfo.xml

