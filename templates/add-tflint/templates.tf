locals {

  ##
  ## Recommended abbreviations for Azure resource types
  ## link : https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations
  ##

  # --------------------------
  # Template General
  # --------------------------

  # API management service instance
  # tflint-ignore: terraform_unused_declarations
  tplgen_api_management_service_instance = "apim-%s"

  # Managed Identity
  # tflint-ignore: terraform_unused_declarations
  tplgen_managed_identity = "id-%s"

  # Management group
  # tflint-ignore: terraform_unused_declarations
  tplgen_management_group = "mg-%s"

  # Policy definition
  # tflint-ignore: terraform_unused_declarations
  tplgen_policy_definition = "policy-%s"

  # Resource group
  # tflint-ignore: terraform_unused_declarations
  tplgen_resource_group = "rg-%s"


  # --------------------------
  # Template Networking
  # --------------------------

  # Application gateway
  # tflint-ignore: terraform_unused_declarations
  tplnet_application_gateway = "agw-%s"

  # Application security group (ASG)
  # tflint-ignore: terraform_unused_declarations
  tplnet_application_security_group = "asg-%s"

  # Bastion
  # tflint-ignore: terraform_unused_declarations
  tplnet_bastion = "bas-%s"

  # CDN profile
  # tflint-ignore: terraform_unused_declarations
  tplnet_cdn_profile = "cdnp-%s"

  # CDN endpoint
  # tflint-ignore: terraform_unused_declarations
  tplnet_cdn_endpoint = "cdne-%s"

  # Connections
  # tflint-ignore: terraform_unused_declarations
  tplnet_connections = "con-%s"

  # DNS
  # tflint-ignore: terraform_unused_declarations
  tplnet_public_dns = "dnsz-%s"

  # DNS zone
  # tflint-ignore: terraform_unused_declarations
  tplnet_private_dns = "pdnsz-%s"

  # Firewall
  # tflint-ignore: terraform_unused_declarations
  tplnet_firewall = "afw-%s"

  # Firewall policy
  # tflint-ignore: terraform_unused_declarations
  tplnet_firewall_policy = "afwp-%s"

  # ExpressRoute circuit
  # tflint-ignore: terraform_unused_declarations
  tplnet_expressRoute_circuit = "erc-%s"

  # Front Door instance
  # tflint-ignore: terraform_unused_declarations
  tplnet_front_door_instance = "fd-%s"

  # Front Door firewall policy
  # tflint-ignore: terraform_unused_declarations
  tplnet_front_door_firewall_policy = "fdfp-%s"

  # Load balancer (internal)
  # tflint-ignore: terraform_unused_declarations
  tplnet_load_balancer_internal = "lbi-%s"

  # Load balancer (external)
  # tflint-ignore: terraform_unused_declarations
  tplnet_load_balancer_external = "lbe-%s"

  # Load balancer rule
  # tflint-ignore: terraform_unused_declarations
  tplnet_load_balancer_rule = "rule-%s"

  # Local network gateway
  # tflint-ignore: terraform_unused_declarations
  tplnet_local_network_gateway = "lgw-%s"

  # NAT gateway
  # tflint-ignore: terraform_unused_declarations
  tplnet_nat_gateway = "ng-%s"

  # Network interface (NIC)
  # tflint-ignore: terraform_unused_declarations
  tplnet_network_interface = "nic-%s"

  # Network security group (NSG)
  # tflint-ignore: terraform_unused_declarations
  tplnet_network_security_group = "nsg-%s"

  # Network security group (NSG) security rules
  # tflint-ignore: terraform_unused_declarations
  tplnet_network_security_group_security_rules = "nsgsr-%s"

  # Network Watcher
  # tflint-ignore: terraform_unused_declarations
  tplnet_network_watcher = "nw-%s"

  # Private Link
  # tflint-ignore: terraform_unused_declarations
  tplnet_private_link = "pl-%s"

  # Public IP address
  # tflint-ignore: terraform_unused_declarations
  tplnet_public_ip_address = "pip-%s"

  # Public IP address prefix
  # tflint-ignore: terraform_unused_declarations
  tplnet_public_ip_address_prefix = "ippre-%s"

  # Route filter
  # tflint-ignore: terraform_unused_declarations
  tplnet_route_filter = "rf-%s"

  # Route table
  # tflint-ignore: terraform_unused_declarations
  tplnet_route_table = "rt-%s"

  # Service endpoint
  # tflint-ignore: terraform_unused_declarations
  tplnet_service_endpoint = "se-%s"

  # Traffic Manager profile
  # tflint-ignore: terraform_unused_declarations
  tplnet_traffic_manager_profile = "traf-%s"

  # User defined route (UDR)
  # tflint-ignore: terraform_unused_declarations
  tplnet_user_defined_route = "udr-%s"

  # Virtual network
  # tflint-ignore: terraform_unused_declarations
  tplnet_virtual_network = "vnet-%s"

  # Virtual network peering
  # tflint-ignore: terraform_unused_declarations
  tplnet_virtual_network_peering = "peer-%s"

  # Virtual network subnet
  # tflint-ignore: terraform_unused_declarations
  tplnet_virtual_network_subnet = "snet-%s"

  # Virtual WAN
  # tflint-ignore: terraform_unused_declarations
  tplnet_virtual_wan = "vwan-%s"

  # VPN Gateway
  # tflint-ignore: terraform_unused_declarations
  tplnet_vpn_gateway = "vpng-%s"

  # VPN connection
  # tflint-ignore: terraform_unused_declarations
  tplnet_vpn_connection = "vcn-%s"

  # VPN site
  # tflint-ignore: terraform_unused_declarations
  tplnet_vpn_site = "vst-%s"

  # Virtual network gateway
  # tflint-ignore: terraform_unused_declarations
  tplnet_virtual_network_gateway = "vgw-%s"

  # Web Application Firewall (WAF) policy
  # tflint-ignore: terraform_unused_declarations
  tplnet_web_application_firewall_policy = "waf%s"

  # Web Application Firewall (WAF) policy rule group
  # tflint-ignore: terraform_unused_declarations
  tplnet_web_application_firewall_policy_rule_group = "wafrg%s"


  # --------------------------
  # Template Compute and Web
  # --------------------------

  # App Service environment_class
  # tflint-ignore: terraform_unused_declarations
  tplncwe_app_service_environment_class = "ase-%s"

  # App Service plan
  # tflint-ignore: terraform_unused_declarations
  tplncwe_app_service_plan = "plan-%s"

  # Availability set
  # tflint-ignore: terraform_unused_declarations
  tplcwe_availability_set = "avail-%s"

  # Azure Arc enabled server
  # tflint-ignore: terraform_unused_declarations
  tplcwe_azure_arc_enabled_server = "arcs-%s"

  # Azure Arc enabled Kubernetes cluster
  # tflint-ignore: terraform_unused_declarations
  tplcwe_azure_arc_enabled_kubernetes_cluster = "arck%s"

  # Cloud service
  # tflint-ignore: terraform_unused_declarations
  tplcwe_cloud_service = "cld-%s"

  # Disk encryption set
  # tflint-ignore: terraform_unused_declarations
  tplcwe_disk_encryption_set = "des%s"

  # Function app
  # tflint-ignore: terraform_unused_declarations
  tplcwe_function_app = "func-%s"

  # Gallery
  # tflint-ignore: terraform_unused_declarations
  tplcwe_gallery = "gal%s"

  # Managed disk (OS)
  # tflint-ignore: terraform_unused_declarations
  tplcwe_managed_disk_os = "osdisk%s"

  # Managed disk (data)
  # tflint-ignore: terraform_unused_declarations
  tplcwe_managed_disk_data = "disk%s"

  # Notification Hubs
  # tflint-ignore: terraform_unused_declarations
  tplcwe_notification_hubs = "ntf-%s"

  # Notification Hubs namespace
  # tflint-ignore: terraform_unused_declarations
  tplcwe_notification_hubs_namespace = "ntfns-%s"

  # Snapshot
  # tflint-ignore: terraform_unused_declarations
  tplcwe_snapshot = "snap-%s"

  # Static web app
  # tflint-ignore: terraform_unused_declarations
  tplcwe_static_web_app = "stapp-%s"

  # Virtual machine
  # tflint-ignore: terraform_unused_declarations
  tplcwe_virtual_machine = "vm-%s"

  # Virtual machine scale set
  # tflint-ignore: terraform_unused_declarations
  tplcwe_virtual_machine_scale_set = "vmss-%s"

  # VM storage account
  # tflint-ignore: terraform_unused_declarations
  tplcwe_vm_storage_account = "stvm%s"

  # Web app
  # tflint-ignore: terraform_unused_declarations
  tplcwe_web_app = "app-%s"


  # --------------------------
  # Template Containers
  # --------------------------

  # AKS cluster
  # tflint-ignore: terraform_unused_declarations
  tplcon_aks_cluster = "aks-%s"

  # Container registry 
  # tflint-ignore: terraform_unused_declarations
  tplcon_container_registry = "cr%s"

  # Container instance
  # tflint-ignore: terraform_unused_declarations
  tplcon_container_instance = "ci%s"

  # Service Fabric cluster
  # tflint-ignore: terraform_unused_declarations
  tplcon_service_fabric_cluster = "sf-%s"


  # --------------------------
  # Template Databases
  # --------------------------

  # Azure Cosmos DB database
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_cosmos_db_database = "cosmos-%s"

  # Azure Cache for Redis instance
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_cache_for_redis_instance = "redis-%s"

  # Azure SQL Database server
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_sql_database_server = "sql-%s"

  # Azure SQL database
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_sql_database = "sqldb-%s"

  # Azure Synapse Analytics
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_synapse_analytics = "syn%s"

  # Azure Synapse Analytics Workspaces
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_synapse_analytics_workspaces = "synw%s"

  # Azure Synapse Analytics SQL Dedicated Pool
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_synapse_analytics_sql_dedicated_pool = "syndp%s"

  # Azure Synapse Analytics Spark Pool
  # tflint-ignore: terraform_unused_declarations
  tpldat_azure_synapse_analytics_spark_pool = "synsp%s"

  # MySQL database
  # tflint-ignore: terraform_unused_declarations
  tpldat_mysql_database = "mysql-%s"

  # MariaDB database
  # tflint-ignore: terraform_unused_declarations
  tpldat_mariadb_database = "maria-%s"

  # PostgreSQL database
  # tflint-ignore: terraform_unused_declarations
  tpldat_postgresql_database = "psql-%s"

  # SQL Server Stretch Database
  # tflint-ignore: terraform_unused_declarations
  tpldat_sql_server_stretch_database = "sqlstrdb-%s"

  # SQL Managed Instance
  # tflint-ignore: terraform_unused_declarations
  tpldat_sql_managed_instance = "sqlmi-%s"


  # --------------------------
  # Template Storage
  # --------------------------

  # Storage account
  # tflint-ignore: terraform_unused_declarations
  tplsto_storage_account = "st%s"

  # Azure StorSimple
  # tflint-ignore: terraform_unused_declarations
  tplsto_azure_stor_simple = "ssimp%s"


  # --------------------------
  # Template AI and Machine Learning
  # --------------------------  

  # Azure Cognitive Search
  # tflint-ignore: terraform_unused_declarations
  tplmlia_azure_cognitive_search = "srch-%s"

  # Azure Cognitive Services
  # tflint-ignore: terraform_unused_declarations
  tplmlia_azure_cognitive_services = "cog-%s"

  # Azure Machine Learning workspace
  # tflint-ignore: terraform_unused_declarations
  tplmlia_azure_machine_learning_workspace = "mlw-%s"


  # --------------------------
  # Template Analytics and IoT
  # --------------------------  

  # Azure Analysis Services server
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_analysis_services_server = "as%s"

  # Azure Databricks workspace
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_databricks_workspace = "dbw-%s"

  # Azure Stream Analytics
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_stream_analytics = "asa-%s"

  # Azure Data Explorer cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_data_explorer_cluster = "dec%s"

  # Azure Data Explorer cluster database
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_data_explorer_cluster_database = "dedb%s"

  # Azure Data Factory
  # tflint-ignore: terraform_unused_declarations
  tplass_azure_data_factory = "adf-%s"

  # Data Lake Store account
  # tflint-ignore: terraform_unused_declarations
  tplass_data_lake_store_account = "dls%s"

  # Data Lake Analytics account
  # tflint-ignore: terraform_unused_declarations
  tplass_data_lake_analytics_account = "dla%s"

  # Event Hubs namespace
  # tflint-ignore: terraform_unused_declarations
  tplass_event_hubs_namespace = "evhns-%s"

  # Event hub
  # tflint-ignore: terraform_unused_declarations
  tplass_event_hub = "evh-%s"

  # Event Grid domain
  # tflint-ignore: terraform_unused_declarations
  tplass_event_grid_domain = "evgd-%s"

  # Event Grid subscriptions
  # tflint-ignore: terraform_unused_declarations
  tplass_event_grid_subscriptions = "evgs-%s"

  # Event Grid topic
  # tflint-ignore: terraform_unused_declarations
  tplass_event_grid_topic = "evgt-%s"

  # HDInsight - Hadoop cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hdinsight_hadoop_cluster = "hadoop-%s"

  # HDInsight - HBase cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hsinsight_hbase_cluster = "hbase-%s"

  # HDInsight - Kafka cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hdinsight_kafka_cluster = "kafka-%s"

  # HDInsight - Spark cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hdinsight_spark_cluster = "spark-%s"

  # HDInsight - Storm cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hdinsight_storm_cluster = "storm-%s"

  # HDInsight - ML Services cluster
  # tflint-ignore: terraform_unused_declarations
  tplass_hdinsight_ml_services_cluster = "mls-"

  # IoT hub
  # tflint-ignore: terraform_unused_declarations
  tplass_iot_hub = "iot-%s"

  # Provisioning services
  # tflint-ignore: terraform_unused_declarations
  tplass_provisioning_services = "provs-%s"

  # Provisioning services certificate
  # tflint-ignore: terraform_unused_declarations
  tplass_provisioning_services_certificate = "pcert-%s"

  # Power BI Embedded
  # tflint-ignore: terraform_unused_declarations
  tplass_power_bi_embedded = "pbi-%s"

  # Time Series Insights environment_class
  # tflint-ignore: terraform_unused_declarations
  tplass_time_series_insights_environment_class = "tsi-%s"


  # --------------------------
  # Template Azure Virtual Desktop
  # --------------------------  

  # Virtual desktop host pool
  # tflint-ignore: terraform_unused_declarations
  tplavd_virtual_desktop_host_pool = "vdpool-%s"

  # Virtual desktop application group
  # tflint-ignore: terraform_unused_declarations
  tplavd_virtual_desktop_application_group = "vdag-%s"

  # Virtual desktop workspace
  # tflint-ignore: terraform_unused_declarations
  tplavd_virtual_desktop_workspace = "vdws-%s"


  # --------------------------
  # Template Developer tools
  # --------------------------  

  # App Configuration store
  # tflint-ignore: terraform_unused_declarations
  tpldev_app_configuration_store = "appcs-%s"

  # SignalR
  # tflint-ignore: terraform_unused_declarations
  tpldev_signalr = "sigr%s"


  # --------------------------
  # Template Integration
  # --------------------------

  # Integration account
  # tflint-ignore: terraform_unused_declarations
  tplint_integration_account = "ia-%s"

  # Logic apps
  # tflint-ignore: terraform_unused_declarations
  tplint_logic_apps = "logic-%s"

  # Service Bus
  # tflint-ignore: terraform_unused_declarations
  tplint_service_bus = "sb-%s"

  # Service Bus queue
  # tflint-ignore: terraform_unused_declarations
  tplint_service_bus_queue = "sbq-%s"

  # Service Bus topic
  # tflint-ignore: terraform_unused_declarations
  tplint_service_bus_topic = "sbt-%s"


  # --------------------------
  # Template Management and governance
  # --------------------------

  # Automation account
  # tflint-ignore: terraform_unused_declarations
  tplmgo_automation_account = "aa-%s"

  # Application Insights
  # tflint-ignore: terraform_unused_declarations
  tplmgo_application_insights = "aai-%s"

  # Azure Monitor action group
  # tflint-ignore: terraform_unused_declarations
  tplmgo_azure_monitor_action_group = "ag-%s"

  # Azure Purview instance
  # tflint-ignore: terraform_unused_declarations
  tplmgo_azure_purview_instance = "pview-%s"

  # Blueprint
  # tflint-ignore: terraform_unused_declarations
  tplmgo_blueprint = "bp-%s"

  # Blueprint assignment
  # tflint-ignore: terraform_unused_declarations
  tplmgo_blueprint_assignment = "bpa-%s"

  # Key vault
  # tflint-ignore: terraform_unused_declarations
  tplmgo_key_vault = "kv-%s"

  # Log Analytics workspace
  # tflint-ignore: terraform_unused_declarations
  tplmo_log_analytics_workspace = "log-%s"


  # --------------------------
  # Template Migration
  # --------------------------

  # Azure Migrate project
  # tflint-ignore: terraform_unused_declarations
  tplmig_azure_migrate_project = "migr-%s"

  # Database Migration Service instance
  # tflint-ignore: terraform_unused_declarations
  tplmig_database_migration_service_instance = "dms-%s"

  # Recovery Services vault
  # tflint-ignore: terraform_unused_declarations
  tplmig_recovery_services_vault = "rsv-%s"
}

