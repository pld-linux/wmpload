Summary:	PPP network monitor for Window Maker Dock
Summary(pl.UTF-8):   Monitor połączeń ppp dla Doku Window Makera
Name:		wmpload
Version:	0.9.5
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.engr.utk.edu/~mdsmith/pload/%{name}-%{version}.tar.gz
# Source0-md5:	022fb510f586ea38cdd5e829a25464bf
Source1:	%{name}.desktop
Patch0:		%{name}-distclean.patch
URL:		http://www.engr.utk.edu/~mdsmith/pload/
BuildRequires:	XFree86-devel
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmpload is an PPP monitor for Window Maker Dock. It can dislay totals
and current rates for both inbound and outbound data. wmpload was
designed to be portable to any platform that can run pppd and X11, but
for Linux 2.2 any network interface listed in /proc/net/dev can be
also be monitored.

%description -l pl.UTF-8
wmpload jest monitorem połączeń PPP dla Doku Window Makera. Posiada
możliwość wyświetlania całościowych i aktualnych wielkości transferów
danych zarówno przychodzących jak i wychodzących. wmpload został
zaprojektowany w sposób umożliwiający używanie go na każdej
platformie, gdzie są dostępne X11 i pppd. Dodatkowo dla Linuksa 2.2
istnieje możliwość monitorowania każdego interfejsu sieciowego
obecnego w /proc/net/dev.

%prep
%setup -q
%patch0 -p1

%build
./configure
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags} -DLINUXPROC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES CREDITS
%attr(755,root,root) %{_bindir}/wmpload
%{_mandir}/man1/wmpload.1x*
%{_desktopdir}/docklets/wmpload.desktop
