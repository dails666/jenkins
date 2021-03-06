# 门店滞销商品列表及7日均销量、上日库存;两个场景，下方两段需要拼一起
# CC商品滞销


def should_not_sell(source_id, cmid, days_delay, item_cat1_ignores):

    sql1 = '''
        SELECT
        t_sale.foreign_store_id,
        t_sale.foreign_item_id,
        round(t_avg.m, 2) as avg_qty,
        t_inventory.quantity as inventory
        from
        (select
        foreign_store_id,
        foreign_item_id,
        case
            when a <= 0.7 then 'A'
            when (a <= 0.9 and a>0.7) then 'B'
        else 'C' end as m
        from(
        SELECT
            t.foreign_store_id,
            t.foreign_item_id,
            t.total_sale,
            SUM(t.total_sale) OVER (PARTITION BY t.foreign_store_id ORDER BY t.total_sale DESC rows unbounded preceding) as sale_cumsum,
            SUM(t.total_sale) OVER (PARTITION BY t.foreign_store_id ORDER BY t.total_sale DESC rows unbounded preceding)/t1.store_sale as a
            FROM (SELECT
                    foreign_store_id,
                    foreign_item_id,
                    SUM(total_sale) AS total_sale
                    FROM cost_%s
                    WHERE cmid = %s
                        AND date >= (getdate()::date - (59 + %s))
                        AND date <= (getdate()::date - %s)
                        AND foreign_category_lv1 not in %s
                    GROUP BY foreign_store_id, foreign_item_id
                    ORDER BY foreign_store_id, SUM(total_sale) DESC) t
        left join
                (select
                    foreign_store_id,
                    sum(total_sale) store_sale
                    from cost_%s
                    where cmid = %s
                        AND date >= (getdate()::date - (59 + %s))
                        AND date <= (getdate()::date - %s)
                        AND foreign_category_lv1 not in %s
                    group by foreign_store_id
                    having sum(total_sale) != 0) t1
        on t.foreign_store_id = t1.foreign_store_id)) t_sale--销售额ABC
        left join
        (select
        foreign_store_id,
        foreign_item_id,
        case when a <= 0.7 then 'A'
            when (a <= 0.9 and a>0.7) then 'B'
            else 'C' end as m
        from(
            SELECT
                t.foreign_store_id,
                t.foreign_item_id,
                t.total_margin,
                SUM(t.total_margin) OVER (PARTITION BY t.foreign_store_id ORDER BY t.total_margin DESC rows unbounded preceding) as margin_cumsum,
                SUM(t.total_margin) OVER (PARTITION BY t.foreign_store_id ORDER BY t.total_margin DESC rows unbounded preceding)/t1.store_margin as a
                FROM (SELECT
                        foreign_store_id,
                        foreign_item_id,
                        SUM(total_sale - total_cost) AS total_margin
                        FROM cost_%s
                        WHERE cmid = %s
                            AND date >= (getdate()::date - (59 + %s))
                            AND date <= (getdate()::date - %s)
                            AND foreign_category_lv1 not in %s
                        GROUP BY foreign_store_id, foreign_item_id
                        ORDER BY foreign_store_id, SUM(total_sale - total_cost) DESC) t
                left join
                    (select
                        foreign_store_id,
                        sum(total_sale - total_cost) store_margin
                        from cost_%s
                        where cmid = %s
                            AND date >= (getdate()::date - (59 + %s))
                            AND date <= (getdate()::date - %s)
                          and foreign_category_lv1 not in %s
                        group by foreign_store_id
                        having sum(total_sale - total_cost) != 0) t1
                on t.foreign_store_id = t1.foreign_store_id)) t_margin--毛利额ABC
        on t_sale.foreign_store_id = t_margin.foreign_store_id and t_sale.foreign_item_id = t_margin.foreign_item_id
        left join
        (select
        foreign_store_id,
        foreign_item_id,
        quantity
        from inventory_%s
        where cmid = %s
            and date = (getdate()::date)) t_inventory--上日库存
        on t_sale.foreign_store_id = t_inventory.foreign_store_id and t_sale.foreign_item_id = t_inventory.foreign_item_id
        left join
        (select
        foreign_store_id,foreign_item_id,sum(total_quantity) / 7 m
        from cost_%s
        where date <= (getdate()::date - %s)
            and date >=(getdate()::date - (6+%s))
        group by foreign_store_id,foreign_item_id) t_avg--7日均销量
        on t_sale.foreign_store_id = t_avg.foreign_store_id and t_sale.foreign_item_id = t_avg.foreign_item_id
        where t_sale.m = 'C' and t_margin.m = 'C'
        and t_inventory.quantity > 0;
        ''' % (source_id,cmid,days_delay,days_delay,item_cat1_ignores,source_id,cmid,days_delay,days_delay,item_cat1_ignores,source_id,cmid,days_delay,days_delay,item_cat1_ignores,source_id,cmid,days_delay,days_delay,item_cat1_ignores,source_id,cmid,source_id,ays_delay,days_delay)


        ### 最近6个月有销售，最近1个月无销售的滞销品
    sql2 = '''
        SELECT
        t1.foreign_store_id,
        t1.foreign_item_id,
        round(t4.m,2) as avg_qty,
        t3.quantity as inventory
        from
        (select
        foreign_store_id,foreign_item_id,sum(total_sale) s
        from cost_%s
        where cmid = %s
            AND date >= (getdate()::date - 180)
            AND date <= (getdate()::date - %s)
        group by foreign_store_id,foreign_item_id) t1 --最近6个月有销售的商品
        left join
        (select
        foreign_store_id,foreign_item_id,sum(total_sale) s
        from cost_%s
        where cmid = %s
            AND date >= (getdate()::date - 60)
            AND date <= (getdate()::date - %s)
        group by foreign_store_id,foreign_item_id) t2 --最近1个月有销售的商品
        on t1.foreign_store_id = t2.foreign_store_id and t1.foreign_item_id = t2.foreign_item_id
        left join
        (select
        foreign_store_id,
        foreign_item_id,
        quantity
        from inventory_%s
        where cmid = %s
            and date = (getdate()::date)) t3 --上日库存
        on t1.foreign_store_id = t3.foreign_store_id and t1.foreign_item_id = t3.foreign_item_id
        left join
        (select
        foreign_store_id,foreign_item_id,sum(total_quantity) / 7 m
        from cost_%s
        where date <= (getdate()::date - %s)
            and date >= (getdate()::date - (6 + %s))
        group by foreign_store_id,foreign_item_id) t4 --7日均销量
        on t1.foreign_store_id = t4.foreign_store_id and t1.foreign_item_id = t4.foreign_item_id
        where t2.s is null
        and quantity > 0
        ''' % (source_id, cmid, days_delay, source_id, cmid, days_delay, source_id, cmid, source_id, days_delay, days_delay)
    sql = sql1+'join'+sql2
    return sql