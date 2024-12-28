import uuid
import qrcode
import os

class Pix():
    def __init__(self):
        pass

    def create_payment(self):
        # Criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # Código do copia e cola
        hash_payment = f"hash_payment_{bank_payment_id}"
        
        # Criação do QR Code
        img = qrcode.make(hash_payment)

        # Criação do caminho onde salvar o QR Code
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.abspath(os.path.join(current_dir, '..'))
        static_img_dir = os.path.join(base_dir, "static", "img")
        os.makedirs(static_img_dir, exist_ok=True)
        qr_code_path = os.path.join(static_img_dir, f"qr_code_payment_{bank_payment_id}.png")

        # Salvar a imagem como arquivo PNG
        img.save(qr_code_path)
        
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}"
        }