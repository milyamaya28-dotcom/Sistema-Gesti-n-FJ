from sistema_logs import SistemaLogs
from excepciones_personalizadas import *
from entidades import Entidad, Cliente
from servicios import Servicio, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from gestor_sistema import GestorSistema


def main():
    print("="*50)
    print("    SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("="*50)

    sistema = GestorSistema()
    operaciones_exitosas = 0
    operaciones_fallidas = 0

    # ═══════ OPERACIÓN 1: Registrar cliente válido ═══════
    print("\n📌 Operación 1: Registrar cliente válido")
    try:
        c1 = Cliente("1001", "María López", "maria@email.com", "3101234567")
        sistema.registrar_cliente(c1)
        print(f"✅ {c1.mostrar_informacion()}")
        operaciones_exitosas += 1
    except DatoInvalidoError as e:
        print(f"❌ Error: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 2: Cliente con correo inválido ═══════
    print("\n📌 Operación 2: Cliente con correo inválido")
    try:
        c2 = Cliente("1002", "Juan Pérez", "correo_invalido", "3209876543")
        sistema.registrar_cliente(c2)
        print(f"✅ {c2.mostrar_informacion()}")
        operaciones_exitosas += 1
    except DatoInvalidoError as e:
        print(f"❌ Error capturado: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 3: Registrar segundo cliente válido ═══════
    print("\n📌 Operación 3: Registrar segundo cliente")
    try:
        c3 = Cliente("1003", "Carlos Ruiz", "carlos@email.com", "3151112222")
        sistema.registrar_cliente(c3)
        print(f"✅ {c3.mostrar_informacion()}")
        operaciones_exitosas += 1
    except DatoInvalidoError as e:
        print(f"❌ Error: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 4: Cliente duplicado ═══════
    print("\n📌 Operación 4: Intentar registrar cliente duplicado")
    try:
        c_dup = Cliente("1001", "Otra Persona", "otra@email.com", "3000000000")
        sistema.registrar_cliente(c_dup)
        print(f"✅ Cliente registrado")
        operaciones_exitosas += 1
    except ClienteDuplicadoError as e:
        print(f"❌ Error capturado: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 5: Registrar servicios ═══════
    print("\n📌 Operación 5: Registrar servicios disponibles")
    try:
        sala = ReservaSalas("S001", "Sala de Conferencias", "Capacidad para 50 personas", 50.0, 50)
        equipo = AlquilerEquipos("S002", "Proyector HD", "Equipo audiovisual", 15.0, 10)
        asesoria = AsesoriaEspecializada("S003", "Asesoría en TI", "Consultoría profesional", 80.0, "Ing. Roberto Gómez")
        
        sistema.registrar_servicio(sala)
        sistema.registrar_servicio(equipo)
        sistema.registrar_servicio(asesoria)
        
        print(f"✅ {sala.describir_servicio()}")
        print(f"✅ {equipo.describir_servicio()}")
        print(f"✅ {asesoria.describir_servicio()}")
        operaciones_exitosas += 1
    except ErrorSistemaFJ as e:
        print(f"❌ Error: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 6: Crear reserva válida ═══════
    print("\n📌 Operación 6: Crear reserva válida")
    try:
        reserva1 = sistema.crear_reserva("1001", "S001", 3)
        reserva1.confirmar()
        print(reserva1.mostrar_detalle())
        costo = reserva1.obtener_costo_total()
        print(f"💰 Costo total: ${costo:.2f}")
        operaciones_exitosas += 1
    except ErrorSistemaFJ as e:
        print(f"❌ Error: {e}")
        operaciones_fallidas += 1

    # ═══════ OPERACIÓN 7: Reserva con cliente inexistente ═══════
    print("\n📌 Operación 7: Reserva con cliente que no existe")
    try:
        reserva2 = sistema.crear_reserva("9999", "S002", 2)
        print(f"✅ Reserva creada")
        operaciones_exitosas += 1
    except DatoInvalidoError as e:
         print(f"❌ Error capturado: {e}")
         operaciones_fallidas += 1
     # ═══════ OPERACIÓN 8: Cancelar reserva ═══════
    print("\n📌 Operación 8: Cancelar reserva")
    try:
         reserva1.cancelar()
         print("✅ Reserva cancelada correctamente")
         operaciones_exitosas += 1
    except EstadoInvalidoError as e:
         print(f"❌ Error: {e}")
         operaciones_fallidas += 1
     # ═══════ OPERACIÓN 9: Cálculo con descuento (polimorfismo) ═══════
    print("\n📌 Operación 9: Cálculo con descuento")
    try:
         servicio = sistema._servicios["S003"]
         costo_con_descuento = servicio.calcular_costo(2, descuento=0.10)
         print(f"✅ Costo con 10% de descuento: ${costo_con_descuento:.2f}")
         operaciones_exitosas += 1
    except ErrorSistemaFJ as e:
         print(f"❌ Error: {e}")
         operaciones_fallidas += 1
     # ═══════ OPERACIÓN 10: Listar todo el sistema ═══════
    print("\n📌 Operación 10: Listar todos los registros")
    print("\n👥 CLIENTES:")
    for c in sistema.listar_clientes():
         print(f"  → {c.mostrar_informacion()}")
     
    print("\n🛎️ SERVICIOS:")
    for s in sistema.listar_servicios():
         print(f"  → {s.describir_servicio()}")
     
    print("\n📅 RESERVAS:")
    for r in sistema.listar_reservas():
         print(r.mostrar_detalle())
     
    operaciones_exitosas += 1
     # ═══════ RESUMEN FINAL ═══════
    print("\n" + "="*50)
    print(f"✅ OPERACIONES EXITOSAS: {operaciones_exitosas}")
    print(f"❌ OPERACIONES FALLIDAS: {operaciones_fallidas}")
    print("📄 Archivo de registros generado: sistema_logs.txt")
    print("="*50)
    SistemaLogs.info(f"=== FIN DEL PROGRAMA - Éxitos: {operaciones_exitosas}, Fallidas: {operaciones_fallidas} ===")
 # Ejecutar el programa
    if __name__ == "__main__":
     main()
     input("\nPresione Enter para salir...")
        


