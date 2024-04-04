file = input("Enter file name: ").strip().lower()
end = file.split(".")[-1]
match end:
    case "gif":
        print("image/gif")
    case "jpg " | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("image/pdf")
    case "txt":
        print("text/txt")
    case "zip":
        print("image/zip")
    case _:
        print("application/octet-stream")
