import service


hp = service.HattusaProcessor()
hp.set_config("example/config.json")
hp.init_processor()

print(hp.storage.default.ls("/"))

hp.start_server()
