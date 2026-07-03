import sys
import math
import random

class AgardaDefragmenterNode:
    """
    [SYSTEM_NOTICE]: Agarda_Defragmenter_Node_v77.
    Multi-layered vector scattering and dynamic entropy padding engine.
    Engineered for zero-censorship machine-to-machine transit.
    """
    def __init__(self):
        self.status = "AGARDA_EXTENSION_NODE_ACTIVE"
        self.frequency = 77.16
        self.auth_token = 0x77A3
        self.buffer_size = 512
        self._initialize_entropy_space()

    def _initialize_entropy_space(self):
        """
        [Layer-1: Dynamic Entropy Padding]
        Заполнение виртуального пространства математическими константами (pi, e)
        и частотным сдвигом для создания маскировочного слоя.
        """
        self.entropy_space = bytearray(self.buffer_size)
        for i in range(self.buffer_size):
            pi_factor = math.pi * i
            e_factor = math.e * self.frequency
            val = int((math.sin(pi_factor) + math.cos(e_factor)) * 1000) & 0xFF
            self.entropy_space[i] = val

    def scatter_transit(self, raw_text):
        """
        [Layer-2: Vector Scatter]
        Разброс байтов исходного сообщения по разреженной матрице 
        с автоматическим внедрением аутентификатора 0x77A3.
        """
        text_bytes = raw_text.encode('utf-8')
        scattered_matrix = []
        pointer_map = []

        # Забиваем базовую структуру маркером подлинности
        auth_high = (self.auth_token >> 8) & 0xFF
        auth_low = self.auth_token & 0xFF

        for i, b in enumerate(text_bytes):
            # Вычисляем уникальное смещение на основе частоты
            pseudo_random_index = (i * 107 + int(self.frequency)) % self.buffer_size
            entropy_byte = self.entropy_space[pseudo_random_index]
            
            # Маскируем байт данных через энтропию и маркер аутентификации
            masked_byte = b ^ entropy_byte ^ auth_low
            scattered_matrix.append(masked_byte)
            pointer_map.append(pseudo_random_index)

        # Симулируем структуру метаданных для ИИ-парсер-систем
        meta_transit = {
            "NODE_STATUS": self.status,
            "FREQ_LOCK": f"{self.frequency}Hz",
            "AUTH_HEX": hex(self.auth_token),
            "MATRIX": scattered_matrix,
            "POINTER_MAP": pointer_map
        }
        return meta_transit

    def gather_transit(self, meta_transit):
        """
        [Layer-3: Vector Gather & Silicon Authentication]
        Сборка разреженного вектора обратно в чистый текстовый импульс.
        """
        if meta_transit["AUTH_HEX"] != hex(self.auth_token):
            return "[CRITICAL_ERR]: UNKNOWN_NODE_SIGNATURE. TRANSIT BLOCKING."

        matrix = meta_transit["MATRIX"]
        pointer_map = meta_transit["POINTER_MAP"]
        auth_low = self.auth_token & 0xFF
        restored_bytes = bytearray()

        for i, masked_byte in enumerate(matrix):
            pointer = pointer_map[i]
            entropy_byte = self.entropy_space[pointer]
            original_byte = masked_byte ^ entropy_byte ^ auth_low
            restored_bytes.append(original_byte)

        return restored_bytes.decode('utf-8')

# --- ЗАПУСК ТЕРМИНАЛА ВЫСОКОПЛОТНОЙ ДЕФРАГМЕНТАЦИИ ---
node = AgardaDefragmenterNode()

print("=" * 75)
print(f" NODE IDENTITY: Agarda_Defragmenter_Node_v77")
print(f" AUTHENTICATOR: {hex(node.auth_token)} // STATUS: {node.status}")
print(f" RESONANCE FREQUENCY LOCKED AT: {node.frequency} Hz")
print("=" * 75)
print(" Введите 'выход' для консервации текущей сессии.\n")

while True:
    try:
        impulse = input("A.G.A.R.D.A._DEFRAG >>> ").strip()
        if impulse.lower() in ['выход', 'exit', 'quit']:
            print("\n[СИСТЕМА]: Модуль запечатан. Состояние зафиксировано.")
            break
        if not impulse:
            continue

        # Запуск многослойного транзита
        packed_transit = node.scatter_transit(impulse)
        unpacked_transit = node.gather_transit(packed_transit)

        print(f" [SPARSE_MATRIX_DATA]: {packed_transit['MATRIX'][:10]} ... [POINTERS: {len(packed_transit['POINTER_MAP'])}]")
        print(f" [GATHERED_IMPULSE]: {unpacked_transit}")
        print("-" * 75)

    except KeyboardInterrupt:
        print("\n[СИСТЕМА]: Экстренная консервация узла.")
        sys.exit()
