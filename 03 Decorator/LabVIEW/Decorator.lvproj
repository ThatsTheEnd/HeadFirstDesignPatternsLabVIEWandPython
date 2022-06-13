<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="21008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Base Class" Type="Folder">
			<Item Name="Beverage.lvclass" Type="LVClass" URL="../Beverage/Beverage.lvclass"/>
			<Item Name="CondimentDecorator.lvclass" Type="LVClass" URL="../CondimentDecorator/CondimentDecorator.lvclass"/>
		</Item>
		<Item Name="Condiments" Type="Folder">
			<Item Name="Mocha.lvclass" Type="LVClass" URL="../Mocha/Mocha.lvclass"/>
		</Item>
		<Item Name="Drinks" Type="Folder">
			<Item Name="Espresso.lvclass" Type="LVClass" URL="../Espresso/Espresso.lvclass"/>
		</Item>
		<Item Name="Serving Coffee.vi" Type="VI" URL="../Serving Coffee.vi"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
