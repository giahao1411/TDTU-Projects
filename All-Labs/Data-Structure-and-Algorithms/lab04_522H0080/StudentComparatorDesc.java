class StudentComparatorDesc extends StudentComparatorAsc {
    public int compare(Student stu1, Student stu2) {
        return -super.compare(stu1, stu2);
    }
}
