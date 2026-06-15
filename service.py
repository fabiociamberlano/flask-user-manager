from db import get_conn

def lista_persone(nome=None, eta=None):

    try:
        conn = get_conn()
        cursor = conn.cursor()

        query = "SELECT * FROM persone WHERE 1=1"
        params = []

        if nome:
            query += " AND nome = ?"
            params.append(nome)

        if eta:
            query += " AND eta = ?"
            params.append(eta)

        cursor.execute(query, params)
        rows = cursor.fetchall()

        conn.close()

        persone = []
        for r in rows:
            persone.append({
                "id": r[0],
                "nome": r[1],
                "eta": r[2]
            })

        return persone

    except Exception as e:
        raise Exception(f"DB error GET: {str(e)}")



def crea_persona(nome, eta):

    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO persone (nome, eta) VALUES (?, ?)",
            (nome, eta)
        )

        conn.commit()
        conn.close()

        return True

    except Exception as e:
        raise Exception(f"DB error INSERT: {str(e)}")



def modifica_persona(id, nome, eta):

    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM persone WHERE id = ?", (id,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return False, "not_found"

        cursor.execute("""
            UPDATE persone
            SET nome = ?, eta = ?
            WHERE id = ?
        """, (nome, eta, id))

        conn.commit()
        conn.close()

        return True, None

    except Exception as e:
        raise Exception(f"DB error UPDATE: {str(e)}")



def elimina_persona(id):

    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM persone WHERE id = ?", (id,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return False, "not_found"

        cursor.execute("DELETE FROM persone WHERE id = ?", (id,))

        conn.commit()
        conn.close()

        return True, None

    except Exception as e:
        raise Exception(f"DB error DELETE: {str(e)}")
