# Comandos Básicos de Git

Una guía de referencia rápida con los comandos esenciales de Git, organizados por etapas de flujo de trabajo.

---

## 1. Configuración Inicial

Configura tu identidad en Git (se aplica a todos los repositorios locales):

```bash
# Definir tu nombre de usuario
git config --global user.name "Tu Nombre"

# Definir tu correo electrónico
git config --global user.email "tu_email@ejemplo.com"

# Ver la configuración actual
git config --list
```

---

## 2. Crear o Clonar Repositorios

```bash
# Iniciar un nuevo repositorio local en la carpeta actual
git init

# Clonar un repositorio remoto existente en tu máquina
git clone <URL_DEL_REPOSITORIO>
```

---

## 3. Estado y Registro de Cambios

```bash
# Ver el estado de los archivos (modificados, en stage o sin seguimiento)
git status

# Ver diferencias detalladas de los archivos modificados
git diff

# Ver el historial de commits
git log

# Ver el historial de commits resumido en una línea por commit
git log --oneline --graph --all
```

---

## 4. Guardar Cambios (Área de Preparación y Commits)

```bash
# Agregar un archivo específico al área de preparación (stage)
git add nombre-archivo.ext

# Agregar todos los archivos modificados y nuevos al área de preparación
git add .

# Guardar los cambios preparados con un mensaje descriptivo
git commit -m "Mensaje descriptivo del cambio"

# Agregar archivos modificados y hacer commit en un solo paso (no incluye archivos nuevos no rastreados)
git commit -am "Mensaje del commit"
```

---

## 5. Ramas (Branches)

```bash
# Listar todas las ramas locales
git branch

# Crear una nueva rama
git branch nombre-de-la-rama

# Cambiarte a una rama existente
git checkout nombre-de-la-rama
# Alternativa moderna:
git switch nombre-de-la-rama

# Crear y cambiarte a una nueva rama en un solo paso
git checkout -b nueva-rama
# Alternativa moderna:
git switch -c nueva-rama

# Unir (merge) los cambios de otra rama en tu rama actual
git merge nombre-de-la-rama

# Eliminar una rama local ya fusionada
git branch -d nombre-de-la-rama
```

---

## 6. Sincronización Remota (GitHub, GitLab, etc.)

```bash
# Vincular un repositorio remoto a tu repositorio local
git remote add origin <URL_DEL_REPOSITORIO>

# Ver los repositorios remotos configurados
git remote -v

# Descargar y fusionar los cambios del repositorio remoto
git pull origin <rama>

# Subir tus commits locales al repositorio remoto
git push origin <rama>

# Subir por primera vez una rama nueva y configurar el seguimiento remoto
git push -u origin main
```

---

## 7. Deshacer Cambios

```bash
# Descartar cambios locales no preparados en un archivo
git restore nombre-archivo.ext

# Sacar un archivo del área de preparación sin perder tus modificaciones
git restore --staged nombre-archivo.ext

# Crear un nuevo commit que revierte los cambios de un commit previo
git revert <ID_DEL_COMMIT>
```

---

## 💡 Flujo Básico Típico de Trabajo

```bash
# 1. Traer últimas actualizaciones
git pull origin main

# 2. Hacer modificaciones en tu código y revisarlas
git status

# 3. Preparar los archivos
git add .

# 4. Confirmar los cambios
git commit -m "feat: agrega nueva funcionalidad"

# 5. Subir los cambios a la nube
git push origin main
```