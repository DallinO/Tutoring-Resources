﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Abstraction
{
    internal class Video
    {
        public string _title;
        public string _author;
        public float _length;
        public List<Comment> _comments = new();

        public Video(string title, string author, float length)
        {
            _title = title;
            _author = author;
            _length = length;
        }

        public int GetCommentCount()
        {
            return _comments.Count;
        }

        public void DisplayVideo()
        {
            Console.WriteLine($"Title: {_title}");
            Console.WriteLine($"Author: {_author}");
            Console.WriteLine($"Length: {FormatSeconds(_length)}");
            Console.WriteLine($"Comment Count: {GetCommentCount()}");
            foreach (Comment comment in _comments)
            {
                comment.DisplayComment();
            }
            Console.WriteLine();
        }

        public void AddComment(Comment comment)
        {
            _comments.Add(comment);
        }

        public string FormatSeconds(float totalSeconds)
        {
            int minutes = (int)totalSeconds / 60;
            int seconds = (int)totalSeconds % 60;
            string formattedTime = $"{minutes:D2}:{seconds:D2}";
            return formattedTime;
        }
    }
}
