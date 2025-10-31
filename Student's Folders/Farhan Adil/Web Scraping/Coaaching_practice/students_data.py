


Students_Data = [
    {
        "Roll no": "01",
        "First Name": "Farhan",
        "Last Name": "Adil",
        "Father Name": "Adil Umar",
        "Class": "Python",
    },
    {
        "Roll no": "02",
        "First Name": "Abdul",
        "Last Name": "Wahab",
        "Father Name": "Abdul Sattar",
        "Class": "Python",
    },
    {
        "Roll no": "03",
        "First Name": "Abdur",
        "Last Name": "Rehman",
        "Father Name": "Shakir Ullah",
        "Class": "Python",
    },
    {
        "Roll no": "04",
        "First Name": "Shariq",
        "Last Name": "Shah",
        "Father Name": "Farooq ",
        "Class": "Python",
    },
    {
        "Roll no": "05",
        "First Name": "Asim",
        "Last Name": "Khan",
        "Father Name": "Zahir Hussain",
        "Class": "Python",
    },
    {
        "Roll no": "06",
        "First Name": "Muhammad",
        "Last Name": "Sheraz",
        "Father Name": "Muhammad",
        "Class": "Python",
    },
    {
        "Roll no": "07",
        "First Name": "Maaz",
        "Last Name": "Ahmad",
        "Father Name": "Muhmmad Naeem",
        "Class": "Python",
    },
]
import pandas as pd



df = pd.DataFrame(Students_Data)
out_name = "Students_Data.csv"
df.to_csv(out_name, index=False)
print(f"Wrote {len(df)} rows to '{out_name}'")


if __name__ == "__main__":
    main()
