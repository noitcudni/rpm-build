Name:           kafka-ganglia
Version:       	1.0.0
Release:        1%{?dist}
Summary:        Our custom flume persistent spool channel

License:        GPLv2+
URL: 	        https://latesco.sea.kixeye.com/projects/AE/repos/v3/browse/kafka-ganglia?at=refs%2Fheads%2Fcode-review
Source0:        %{name}.tgz

BuildRequires:  apache-maven
#BuildRoot: %{_tmppath}/%{name}-%{version}

%description


%prep
%setup -n %{name}


%build
mvn clean package

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/kafka/lib
install -m 644 target/%{name}-%{version}-uber.jar $RPM_BUILD_ROOT/usr/lib/kafka/lib/%{name}-%{version}-uber.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/lib/kafka/lib/%{name}-%{version}-uber.jar


%changelog
