from beans.bean_factory import BeanFactory

factory = BeanFactory()
menu = factory.get_menu()

menu.mostrar_menu()
