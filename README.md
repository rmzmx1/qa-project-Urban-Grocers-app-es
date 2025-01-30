# Urban Grocers - QA Project  


## 📌 Descripción del Proyecto  
Este proyecto forma parte del **Sprint 7** y se centra en la automatización de pruebas para la funcionalidad de creación de nuevos usuarios en **Urban Grocers**. El objetivo es validar el comportamiento del campo `name` en la solicitud.  

---


## 📚 Fuente de Documentación  
Este proyecto sigue la documentación basada en **apiDoc**.

---

## 🚀 Tecnologías Utilizadas
- **Python** (para la automatización de pruebas)  
- **Pytest** (para la ejecución de pruebas y validaciones)  
- **Requests Library** (para enviar solicitudes a la API)  
- **GitHub** (para control de versiones)  
- **JSON** (para el manejo de solicitudes y respuestas)  

---

## ✅ Lista de Comprobación de Pruebas  

Los siguientes casos de prueba validan el campo `name` en el cuerpo de la solicitud.  

| №  | Descripción | Resultado Esperado |
|----|------------|--------------------|
| 1  | **Número mínimo de caracteres permitidos (1):** `kit_body = { "name": "a" }` | Código de respuesta: `201` ✅ El campo `name` en la respuesta coincide con la solicitud. |
| 2  | **Número máximo de caracteres permitidos (511):** `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a" }` | Código de respuesta: `201` ✅ El campo `name` en la respuesta coincide con la solicitud. |
| 3  | **Número de caracteres menor al mínimo permitido (0):** `kit_body = { "name": "" }` | Código de respuesta: `400` ❌ |
| 4  | **Número de caracteres mayor al máximo permitido (512):** `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }` | Código de respuesta: `400` ❌ |
| 5  | **Se permiten caracteres especiales:** `kit_body = { "name": ""№%@"," }` | Código de respuesta: `201` ✅ El campo `name` en la respuesta coincide con la solicitud. |
| 6  | **Se permiten espacios:** `kit_body = { "name": " A Aaa " }` | Código de respuesta: `201` ✅ El campo `name` en la respuesta coincide con la solicitud. |
| 7  | **Se permiten números:** `kit_body = { "name": "123" }` | Código de respuesta: `201` ✅ El campo `name` en la respuesta coincide con la solicitud. |
| 8  | **El parámetro `name` no se incluye en la solicitud:** `kit_body = { }` | Código de respuesta: `400` ❌ |
| 9  | **Se envía un tipo de dato diferente (número en lugar de string):** `kit_body = { "name": 123 }` | Código de respuesta: `400` ❌ |

---

## Fin
