# Lab 2

## Author : Strelia Illia

## Group id : IM-23

## This is console application written in Python to convert _Markdown_ file to _HTML_ or _ANSI_ formats

## Requirements: Python 3.X version

## To clone repository

```console
 git clone https://github.com/Moriartymath/Lab_1_2.git
```

## To run application :

- Clone repository.
- Open folder with application.
- Open terminal and run commands described in the next section.

## Input parameterts :

- **_Required argument_** (first parameter) : Path to the input Markdown file

## Optional arguments

### flag --out :

- **_Optional argument_** to specify the output file otherwise converted text will be displayed in console : **Path to the output file**

### flag --format :

- **_Optional argument_** if present the result of executing program will be in HTML format otherwise in ANSI: **Specify the format of resulting text**

## Examples of using:

- ### **With Optional argument**

  #### **flag --out**

  ```console
  python main.py  markdown_file.md --out  text_file.txt
  ```

  - **The result will be in ANSI format and saved to text_file.txt**

  #### **flag --format**

  ```console
  python main.py  markdown_file.md  --format
  ```

  - **The result will be in HTML format in the output of console**

  #### **flag --out and --format**

  ```console
  python main.py  markdown_file.md  --out html_file.html --format
  ```

  - **The result will be in HTML format and saved to the html_file.html**

- ### **Without optional argumenet**

  ```console
  python main.py  markdown_file.md
  ```

  - **The result will be in ANSI format in the output of console**

## Tests :

### **To run all tests use following command**

- ```console
  python -m unittest test_main.py
  ```

### [Link to Revert commit](https://github.com/Moriartymath/Lab-1/commit/eca9676a1811f25032f47c6fdc7d429cf8d10479) - eca9676a1811f25032f47c6fdc7d429cf8d10479

### [Link to CI test failure](https://github.com/Moriartymath/Lab-1/commit/7626db716b5ab3a7357bb729235f58867692a410) - 7626db716b5ab3a7357bb729235f58867692a410

## My thoughts about CI and unit tests

**In my opinion unit tests along with CI is really powerfull and convinient tools to keep track of your application`s stabillity on every step.It`s specially true for big projects due to automatization of all processes provided by CI.**
