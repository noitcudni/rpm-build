Name:           flume-ng-kafka-sink
Version:       	0.1.0
Release:        1%{?dist}
Summary:        flume to kafka 0.8 connector 

License:        GPLv2+
URL:            https://github.com/noitcudni/flume-ng-kafka-sink
Source0:        %{name}-%{version}.tgz

BuildRequires:  apache-maven
Requires: flume

%description


%prep
%setup -q


%build
mvn clean install -Dmaven.test.skip=true -Drat.numUnapprovedLicenses=100

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/flume/lib
install -m 644 target/%{name}-uber-0.8.jar $RPM_BUILD_ROOT/usr/lib/flume/lib/%{name}-uber-0.8.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/lib/flume/lib/%{name}-uber-0.8.jar


%changelog
