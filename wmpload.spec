Summary:	PPP network monitor for Window Maker Dock
Summary(pl):	Monitor po³±czeñ ppp dla Doku Window Makera 
Name:		wmpload 
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.engr.utk.edu/~mdsmith/pload/%{name}-%{version}.tar.gz
Source1:	wmpload.desktop
URL:		http://www.engr.utk.edu/~mdsmith/pload/
BuildRequires:	XFree86-devel
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
wmpload is an PPP monitor for Window Maker Dock. It can dislay totals
and current rates for both inbound and outbound data. wmpload was designed
to be portable to any platform that can run pppd and X11, but for Linux 2.2
any network interface listed in /proc/net/dev can be also be monitored.

%description -l pl
wmpload jest monitorem po³±czeñ PPP dla Doku Window Makera. Posiada
mo¿liwo¶æ wy¶wietlania ca³o¶ciowych i aktualnych wielko¶ci transferów
danych zarówno przychodz±cych jak i wychodz±cych. wmpload zosta³ 
zaprojektowany w sposób umo¿liwiaj±cy u¿ywanie go na ka¿dej platformie,
gdzie s± dostêpne X11 i pppd. Dodatkowo dla Linuksa 2.2 istnieje mozliwo¶æ
monitorowania ka¿dego interfejsu sieciowego obecnego w /proc/net/dev.

%prep
%setup -q

%build
./configure
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README CHANGES CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,CREDITS}.gz
%attr(755,root,root) %{_bindir}/wmpload

%{_mandir}/man1/wmpload.1x.gz
%{_applnkdir}/DockApplets/wmpload.desktop
