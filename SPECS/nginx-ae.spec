%define echo_nginx_module echo-nginx-module-0.51
%define nginx_prefix /opt/nginx

Name:           nginx-ae
Version:        1.5.7
Release:        1%{?dist}
Summary:       	nginx 1.5.7 + echo module 0.51

License:        GPLv2+
Source0:        nginx-1.4.2.tar.gz
Source1:        echo-nginx-module-0.51.tar.gz

BuildRequires:  pcre-devel

%description


%prep
%setup -n nginx-1.4.2 


%build
tar xvzf $RPM_SOURCE_DIR/%{echo_nginx_module}.tar.gz -C $RPM_BUILD_DIR
./configure --prefix=%{nginx_prefix} --add-module=$RPM_BUILD_DIR/%{echo_nginx_module}
make -j2


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{nginx_prefix}/logs/
%{nginx_prefix}/conf/fastcgi.conf
%{nginx_prefix}/conf/fastcgi.conf.default
%{nginx_prefix}/conf/fastcgi_params
%{nginx_prefix}/conf/fastcgi_params.default
%{nginx_prefix}/conf/koi-utf
%{nginx_prefix}/conf/koi-win
%{nginx_prefix}/conf/mime.types
%{nginx_prefix}/conf/mime.types.default
%{nginx_prefix}/conf/nginx.conf
%{nginx_prefix}/conf/nginx.conf.default
%{nginx_prefix}/conf/scgi_params
%{nginx_prefix}/conf/scgi_params.default
%{nginx_prefix}/conf/uwsgi_params
%{nginx_prefix}/conf/uwsgi_params.default
%{nginx_prefix}/conf/win-utf
%{nginx_prefix}/html/50x.html
%{nginx_prefix}/html/index.html
%{nginx_prefix}/sbin/nginx

%changelog
