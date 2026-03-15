from qa_chain import get_qa_chain


def main():

    qa = get_qa_chain()

    print("Government Reports QA System")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Question: ")

        if query.lower() == "exit":
            break

        answer = qa.invoke(query)

        print("\nAnswer:\n")
        print(answer)
        print("\n")


if __name__ == "__main__":
    main()