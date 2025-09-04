## ✅ Основы LaTeX в Obsidian

- **Встроенная формула**: `$ ... $` → отображается **в строке**  
    Пример: `$a^2 + b^2 = c^2$` → a2+b2=c2a^2 + b^2 = c^2
    
- **Блочная формула**: `$$ ... $$` → **отдельная строка по центру**  
    Пример:
    
    ```latex
    $$
    \int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}
    $$
    ```
    

## ✅ Греческие буквы

| Буква | Код      | Пример  |
| ----- | -------- | ------- |
| α     | `\alpha` | α\alpha |
| β     | `\beta`  | β\beta  |
| γ     | `\gamma` | γ\gamma |
| Δ     | `\Delta` | Δ\Delta |
| π     | `\pi`    | π\pi    |
| Ω     | `\Omega` | Ω\Omega |

---

## ✅ Верхние и нижние индексы

- Степени: `x^2` → x2x^2
    
- Индексы: `a_1` → a1a_1
    
- Комбинация: `x_{i}^{2}` → xi2x_i^2
    

---

## ✅ Скобки

- `(a+b)` → (a+b)(a+b)
    
- `\left( a + b \right)` → большие скобки: (a+b)\left( a + b \right)
    
- Другие:  
    `\{a\}` → {a}\{a\}  
    `\langle a \rangle` → ⟨a⟩\langle a \rangle
    

---

## ✅ Операции

|Операция|Код|Пример|
|---|---|---|
|Сумма|`\sum_{i=1}^n x_i`|∑i=1nxi\sum_{i=1}^n x_i|
|Произведение|`\prod_{i=1}^n a_i`|∏i=1nai\prod_{i=1}^n a_i|
|Интеграл|`\int_a^b f(x)\,dx`|∫abf(x) dx\int_a^b f(x)\,dx|
|Лимит|`\lim_{x\to0} f(x)`|lim⁡x→0f(x)\lim_{x\to0} f(x)|

---

## ✅ Дроби и корни

- `\frac{a}{b}` → ab\frac{a}{b}
    
- `\sqrt{x}` → x\sqrt{x}
    
- `\sqrt[n]{x}` → xn\sqrt[n]{x}
    

---

## ✅ Матричный формат

```latex
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
```

[abcd]\begin{bmatrix} a & b \\ c & d \end{bmatrix}

---

## ✅ Стрелки и знаки

| Символ | Код               | Пример           |
| ------ | ----------------- | ---------------- |
| →      | `\to`             | →\to             |
| ⇒      | `\Rightarrow`     | ⇒\Rightarrow     |
| ←      | `\leftarrow`      | ←\leftarrow      |
| ⇔      | `\Leftrightarrow` | ⇔\Leftrightarrow |
| ∈      | `\in`             | ∈\in             |
| ∉      | `\notin`          | ∉\notin          |
| ⊂      | `\subset`         | ⊂\subset         |
| ⊆      | `\subseteq`       | ⊆\subseteq       |

---

## ✅ Выравнивание уравнений

```latex
\begin{align}
a + b &= c \\
x &= y + z
\end{align}
```

---

## ✅ Текст в формулах

- `\text{текст}` → текст\text{текст}
    
- Пример: `\text{если } x > 0`
    

---

## ✅ Популярные конструкции

|Формула|Код|
|---|---|
|x∈Rx \in \mathbb{R}|`x \in \mathbb{R}`|
|∀x∃y\forall x \exists y|`\forall x \exists y`|
|≈,∼,≠\approx, \sim, \neq|`\approx`, `\sim`, `\neq`|
|x^,xˉ,x~\hat{x}, \bar{x}, \tilde{x}|`\hat{x}`, `\bar{x}`, `\tilde{x}`|

---

### ✅ 1. Простая матрица (без скобок)

```latex
$$
\begin{matrix}
a & b \\
c & d
\end{matrix}
$$
```

Результат:

$\begin{matrix} a & b \\ c & d \end{matrix}$

---

### ✅ 2. Матрица с квадратными скобками

```latex
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$
```

[abcd]\begin{bmatrix} a & b \\ c & d \end{bmatrix}

---

### ✅ 3. Матрица с круглыми скобками

```latex
$$
\begin{pmatrix}
a & b & c \\
d & e & f
\end{pmatrix}
$$
```

(abcdef)\begin{pmatrix} a & b & c \\ d & e & f \end{pmatrix}

---

### ✅ 4. Матрица с фигурными скобками

```latex
$$
\begin{Bmatrix}
a & b \\
c & d
\end{Bmatrix}
$$
```

{abcd}\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}

---

### ✅ 5. С номерами строк/столбцов (лучше для учебы)

```latex
$$
\begin{array}{c|ccc}
    & 1 & 2 & 3 \\
\hline
1 & a & b & c \\
2 & d & e & f
\end{array}
$$
```

1231abc2def\begin{array}{c|ccc} & 1 & 2 & 3 \\ \hline 1 & a & b & c \\ 2 & d & e & f \end{array}

---

### ✅ 6. Добавить многоточия

- `\cdots` → горизонтальное многоточие
    
- `\vdots` → вертикальное
    
- `\ddots` → диагональное
    

Пример:

```latex
$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$
```

---

Хочешь, я добавлю **в твою шпаргалку отдельный блок “Матрицы” с примерами** и сделаю **полный MD-файл для Obsidian**, который включает:  
✔ основные команды  
✔ все символы  
✔ матрицы  
✔ примеры выравнивания?

Могу прямо сейчас сгенерировать готовый `.md` файл. Нужно?