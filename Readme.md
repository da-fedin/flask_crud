# Flask CRUD application

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2023-06-23/homework__dmytro_fedin__8_flask/actions/workflows/main-workflow.yml/badge.svg)

## 🏠 Create/Read/Update/Delete

Simple flask project to manage with the simplest phonebook stored in database.

## 🏠 Usage

After project run make the following actions for CRUD:
- Create record

```
http://127.0.0.1:5000/item/add?name=Name&number=123456789
```

- Read record

```
http://127.0.0.1:5000/item/read/<int:pk>
```

- Update record

```
http://127.0.0.1:5000/item/update/<int:pk>?name=new_ame&number=123456789
```

- Delete record

```
http://127.0.0.1:5000/item/delete/<int:pk>
```

## 🏠 Build


#### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
make d-homework-i-run
```

#### 🚮 Purge

Make all actions needed for stop homework from zero.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

#### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

#### ⚙️ Configure

Configure homework.

```shell
make init-configs
```

---

## 🐳 Docker

Use services in dockers.

#### ▶️ Run

Just run

```shell
make d-run
```

#### ⏹️Stop

Stop services

```shell
make d-stop
```

#### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```
