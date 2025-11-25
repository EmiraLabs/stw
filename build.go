package main

import (
	"html/template"
	"io/fs"
	"os"
	"path/filepath"
	"strings"
)

type Page struct {
	Title   string
	Content template.HTML
}

func main() {
	tmpl := template.Must(template.ParseFiles("templates/base.html", "templates/components/header.html", "templates/components/footer.html"))

	filepath.WalkDir("pages", func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if d.IsDir() {
			return nil
		}
		if d.Name() == "index.html" {
			rel, _ := filepath.Rel("pages", path)
			dst := filepath.Join("dist", rel)
			os.MkdirAll(filepath.Dir(dst), 0755)

			var title string
			if rel == "index.html" {
				title = "Home"
			} else {
				dir := filepath.Dir(rel)
				title = strings.Title(filepath.Base(dir))
			}

			content, err := os.ReadFile(path)
			if err != nil {
				return err
			}
			page := Page{Title: title, Content: template.HTML(content)}
			f, err := os.Create(dst)
			if err != nil {
				return err
			}
			defer f.Close()
			return tmpl.ExecuteTemplate(f, "base.html", page)
		}
		return nil
	})
}
