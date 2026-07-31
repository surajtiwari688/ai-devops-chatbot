variable "resource_group_name" {
  default = "rg-ai-chatbot-dev"
}

variable "location" {
  default = "Central India"
}

variable "vnet_name" {
  default = "vnet-ai-chatbot"
}

variable "subnet_name" {
  default = "subnet-ai-chatbot"
}

variable "address_space" {
  default = ["10.0.0.0/16"]
}

variable "subnet_prefix" {
  default = ["10.0.1.0/24"]
}
