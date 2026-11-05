%bcond_with javadoc

Name:    jnr-netdb
Version: 1.2.0
Release: 1
Summary: Network services database access for java
Group: Development/Java

License: ASL 2.0
URL:     https://github.com/jnr/%{name}/
Source0: https://github.com/jnr/%{name}/archive/refs/tags/jnr-netdb-%{version}.tar.gz
BuildArch: noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	sonatype-oss-parent
BuildSystem:	maven

BuildRequires: jnr-ffi
BuildRequires: junit

Requires: java
Requires: javapackages-filesystem
Requires: jnr-ffi

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%if %{with javadoc}
%package        javadoc
Summary:        Javadoc for %{name}


%endif
%if %{with javadoc}
%description    javadoc
Javadoc for %{name}.

%endif
%prep
%setup -q -n jnr-netdb-jnr-netdb-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%files -f .mfiles
%doc LICENSE README

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%endif
