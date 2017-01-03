# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 03/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import request, url_for, current_app

from r import R


class PaginatorDataProvider(object):
    def get_data(self, min_page, curr_page, max_page):
        self.paginator_size = current_app.config["PAGINATOR_SIZE"]
        assert self.paginator_size >= 5 and self.paginator_size % 2 == 1
        self.min_page = min_page
        self.curr_page = curr_page
        self.max_page = max_page
        self.n_pages = max_page-min_page+1

        previous_href = None
        if (curr_page > min_page):
            previous_href = self.get_href(curr_page - 1)
        next_href = None
        if (curr_page < max_page):
            next_href = self.get_href(curr_page + 1)

        return dict(
            previous_href=previous_href,
            next_href=next_href,
            pages=self.get_pages()
        )

    def get_pages(self):
        pages = []
        mid_page = (self.min_page + self.max_page)/2
        curr_page_neighbor_size = (self.paginator_size-3)/2
        if self.n_pages <= self.paginator_size:
            for i in range(self.min_page, self.max_page+1):
                pages.append(self.get_page_data(page=i))
            return pages
        elif self.curr_page <= mid_page:
            first_page = self.curr_page-curr_page_neighbor_size
            if first_page <= self.min_page:
                for i in range(self.min_page, self.min_page+self.paginator_size-2):
                    pages.append(self.get_page_data(page=i))
            else:
                for i in range(self.curr_page-curr_page_neighbor_size, self.curr_page+curr_page_neighbor_size+1):
                    pages.append(self.get_page_data(page=i))
            pages.append(self.get_suspension_points())
            pages.append(self.get_page_data(page=self.max_page))
        else:
            last_page = self.curr_page + curr_page_neighbor_size
            if last_page >= self.max_page:
                for i in range(self.max_page - (self.paginator_size-2) + 1, self.max_page+1):
                    pages.append(self.get_page_data(page=i))
            else:
                for i in range(self.curr_page-curr_page_neighbor_size, self.curr_page+curr_page_neighbor_size+1):
                    pages.append(self.get_page_data(page=i))
            pages = [self.get_suspension_points()] + pages
            pages = [self.get_page_data(page=self.min_page)] + pages
        return pages

    def get_page_data(self, page):
        return dict(
            text=page,
            href=self.get_href(page),
            active=page==self.curr_page
        )

    def get_suspension_points(self):
        return dict(
            text="...",
        )

    def get_href(self, page):
        endpoint = request.endpoint
        url_args = dict(request.args, **request.view_args)
        url_args[R.string.page_arg_name] = page
        return url_for(endpoint, **url_args)


paginator_data_provider = PaginatorDataProvider()
