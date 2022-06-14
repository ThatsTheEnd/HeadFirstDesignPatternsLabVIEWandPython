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
		<Item Name="Pizzas" Type="Folder">
			<Property Name="NI.SortType" Type="Int">3</Property>
			<Item Name="Pizza.lvclass" Type="LVClass" URL="../Pizza/Pizza.lvclass"/>
			<Item Name="NYStyleCheesePizza.lvclass" Type="LVClass" URL="../NYStyleCheesePizza/NYStyleCheesePizza.lvclass"/>
			<Item Name="NYStylePepperoniPizza.lvclass" Type="LVClass" URL="../NYStylePepperoniPizza/NYStylePepperoniPizza.lvclass"/>
			<Item Name="ChicagoStyleCheesePizza.lvclass" Type="LVClass" URL="../ChicagoStyleCheesePizza/ChicagoStyleCheesePizza.lvclass"/>
			<Item Name="ChicagoStylePepperoniPizza.lvclass" Type="LVClass" URL="../ChicagoStylePepeproniPizza/ChicagoStylePepperoniPizza.lvclass"/>
		</Item>
		<Item Name="Stores" Type="Folder">
			<Property Name="NI.SortType" Type="Int">3</Property>
			<Item Name="PizzaStore.lvclass" Type="LVClass" URL="../PizzaStore/PizzaStore.lvclass"/>
			<Item Name="NYPizzaStore.lvclass" Type="LVClass" URL="../NYPizzaStore/NYPizzaStore.lvclass"/>
			<Item Name="ChicagoPizzaStore.lvclass" Type="LVClass" URL="../ChicagoPizzaStore/ChicagoPizzaStore.lvclass"/>
		</Item>
		<Item Name="main.vi" Type="VI" URL="../main.vi"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
